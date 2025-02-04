import datetime as dt
import ftplib
import queue
import threading
import time
from functools import lru_cache
from pathlib import Path
from typing import Callable, Iterable

from datasus_fetcher.slicer import Slicer

from . import logger, meta
from .remote_names import get_pattern, parse_filename
from .storage import DataPartition, RemoteFile, get_filename, get_partition_dir

FTP_HOST = "ftp.datasus.gov.br"
MEGA = 1_000_000


class Fetcher(threading.Thread):
    def __init__(
        self,
        q: queue.Queue,
        dest_dir: Path,
        callback: Callable | None = None,
    ):
        super().__init__()
        self.daemon = True
        self.ftp = connect()
        self.q = q
        self.dest_dir = dest_dir
        if callable(callback):
            self.callback = callback
        else:
            self.callback = lambda _: None
        self._kill_event = threading.Event()

    def run(self):
        while not self.dead():
            file: RemoteFile = self.q.get()
            dataset: str = file.dataset
            partition_dir: str = get_partition_dir(file)
            filename: str = get_filename(file)

            filepath: Path = self.dest_dir / dataset / partition_dir / filename
            if filepath.exists() and filepath.stat().st_size == file.size:
                self.q.task_done()
                continue
            filepath.parent.mkdir(parents=True, exist_ok=True)

            try:
                logger.debug("%s -> %s", file.full_path, filepath)
                t0 = time.time()
                fetch_file(self.ftp, file.full_path, filepath)
                tt = time.time() - t0
                log_download(tt, file.size, filepath.name)

                file_metadata = {
                    "url": f"ftp://{FTP_HOST}/{file.full_path}",
                    "size": file.size,
                    "filepath": filepath,
                    "suffix": file.extension,
                    "dataset": dataset,
                    "created_at": file.datetime,
                }

                self.callback(file_metadata)

            except Exception as e:
                logger.exception("Exception %s", e)
            finally:
                self.q.task_done()

    def kill(self) -> None:
        self._kill_event.set()

    def dead(self) -> bool:
        return self._kill_event.is_set()


def log_download(tt: float, size: int, filename: str):
    filesize_mb = size / MEGA
    download_speed_mbps = (size * 8) / tt / MEGA
    log = " ".join(
        [
            f"{filename: <40}",
            f"{filesize_mb: >6.2f} MB",
            f"{tt: >5.2f} s",
            f"{download_speed_mbps: >5.2f} Mb/s",
        ]
    )
    logger.info(log)


def connect() -> ftplib.FTP:
    """Connects to the FTP server."""
    ftp = ftplib.FTP(FTP_HOST, encoding="latin-1")
    ftp.login()
    return ftp


@lru_cache
def list_files(
    ftp: ftplib.FTP,
    directory: str,
    retries: int = 3,
) -> list[dict]:
    try:
        ftp.cwd(directory)
    except ftplib.error_perm:
        logger.exception(f"Directory not found. {directory}")

    files: list[str] = []
    while retries > 0:
        files.clear()
        try:
            ftp.retrlines("LIST", files.append)
            break
        # Timeout exception
        except (ftplib.error_temp, TimeoutError):
            logger.exception("Timeout exception while listing files.")
            retries -= 1
            time.sleep(5)

    # parse files' date, size and name
    def parse_line(line: str) -> dict[str, str | int | dt.datetime | None]:
        date, time, size, name = line.split(maxsplit=3)
        extension = name.rsplit(".", maxsplit=1)[1].lower()
        datetime = dt.datetime.strptime(date + " " + time, "%m-%d-%y %I:%M%p")
        try:
            size = int(size)
        except ValueError:
            size = None
        return {
            "datetime": datetime,
            "size": size,
            "filename": name,
            "extension": extension,
            "full_path": f"{directory}/{name}",
        }

    parsed_files = [parse_line(line) for line in files]

    return parsed_files


def fetch_file(
    ftp: ftplib.FTP,
    path: str,
    dest_filepath: Path | str,
    retries: int = 3,
):
    """Fetch a file from a remote FTP server.

    :param path: The path to the file.
    :param dest_filepath: The destination file path.
    :param ftp: The FTP connection.
    """

    if isinstance(dest_filepath, str):
        dest_filepath = Path(dest_filepath.lower())
    if not dest_filepath.parent.exists():
        dest_filepath.parent.mkdir(parents=True)

    while retries > 0:
        try:
            with open(dest_filepath, "wb") as f:
                ftp.retrbinary("RETR " + path, f.write)
            break
        # File not found exception
        except ftplib.error_perm:
            logger.exception("File %s not found.", path)
            dest_filepath.unlink(missing_ok=True)
            break
        # Timeout exception
        except (ftplib.error_temp, TimeoutError):
            logger.exception("Timeout exception for %s.", path)
            dest_filepath.unlink(missing_ok=True)
            retries -= 1
            time.sleep(5)


def list_dataset_files(ftp: ftplib.FTP, dataset: str) -> list[RemoteFile]:
    dataset_files = []
    for period in meta.datasets[dataset]["periods"]:
        files = [
            RemoteFile(
                filename=f["filename"],
                datetime=f["datetime"],
                size=f["size"],
                extension=f["extension"],
                full_path=f["full_path"],
                dataset=dataset,
                preliminar=period.get("preliminar", False),
            )
            for f in list_files(ftp, directory=period["dir"], retries=3)
        ]
        if not period["filename_pattern"]:
            dataset_files.extend(files)
            continue
        fn_pattern = period["filename_pattern"]
        pattern = get_pattern(period=period)
        for file in files:
            m = pattern.match(file.filename.lower())
            if m:
                file.partition = DataPartition(**parse_filename(m, fn_pattern))
                dataset_files.append(file)
    return dataset_files


def download_data(
    datasets: Iterable[str],
    destdir: Path,
    threads: int = 2,
    callback: Callable | None = None,
    slicer: Slicer | None = None,
):
    """Multithreaded download data files"""
    logger.info("Starting download with %s threads", threads)
    if datasets:
        datasets_ = set(datasets) & set(meta.datasets.keys())
    else:
        datasets_ = meta.datasets.keys()
    ftp0 = connect()
    q = queue.Queue()
    for _ in range(threads):
        _w = Fetcher(q, destdir, callback=callback)
        _w.start()
    for dataset in datasets_:
        logger.info("Listing files of %s", dataset)
        for remote_file in list_dataset_files(ftp0, dataset):
            if slicer is not None and not slicer(remote_file):
                continue
            q.put(remote_file)
    ftp0.close()
    logger.info("Joining queue")
    q.join()
    for th in threading.enumerate():
        if isinstance(th, Fetcher):
            th.ftp.close()


def list_documentation_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    ftp_dir = meta.docs[dataset]["dir"]
    ftp.cwd(ftp_dir)
    files = list_files(ftp, directory=ftp_dir)
    return files


def download_documentation(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):
    destdir = destdir / f"{dataset}[doc]"

    files = list_documentation_files(ftp, dataset)

    for i, file in enumerate(files):
        filename, extension = file["filename"].rsplit(".", 1)
        filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
        filepath = destdir / filename

        # Check if file already exists and has the same size
        if filepath.exists() and filepath.stat().st_size == file["size"]:
            continue

        logger.debug(f"{i: >5} {file['full_path']} -> {filepath}")
        t0 = time.time()
        fetch_file(ftp, file["full_path"], filepath)
        tt = time.time() - t0
        filesize_kb = f"{file['size'] / 1024:.2f} kB"
        download_speed_kbps = f"{file['size'] / tt / 1024:.2f} kB/s"
        logger.debug(
            f"      {filename} {tt:.2f} s {filesize_kb} {download_speed_kbps}",
        )

        file_metadata = {
            "url": f"ftp://{FTP_HOST}/{file['full_path']}",
            "size": file["size"],
            "filepath": filepath,
            "created_at": file["datetime"],
            "suffix": extension,
        }

        yield file_metadata


def list_auxiliary_tables_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    ftp_dir = meta.auxiliary_tables[dataset]["dir"]
    ftp.cwd(ftp_dir)
    files = list_files(ftp, directory=ftp_dir)
    return files


def download_auxiliary_tables(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):
    destdir = destdir / f"{dataset}[aux]"

    files = list_auxiliary_tables_files(ftp, dataset)

    for i, file in enumerate(files):
        filename, extension = file["filename"].rsplit(".", 1)
        filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
        filepath = destdir / filename
        if filepath.exists() and filepath.stat().st_size == file["size"]:
            continue
        logger.debug(f"{i: >5} {file['full_path']} -> {filepath}")
        t0 = time.time()
        fetch_file(ftp, file["full_path"], filepath)
        tt = time.time() - t0
        filesize_kb = f"{file['size'] / 1024:.2f} kB"
        download_speed_kbps = f"{file['size'] / tt / 1024:.2f} kB/s"
        logger.debug(
            f"      {filename} {tt:.2f} s {filesize_kb} {download_speed_kbps}",
        )

        file_metadata = {
            "url": f"ftp://{FTP_HOST}/{file['full_path']}",
            "size": file["size"],
            "filepath": filepath,
            "created_at": file["datetime"],
            "suffix": extension,
        }

        yield file_metadata
