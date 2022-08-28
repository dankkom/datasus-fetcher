import datetime as dt
import hashlib
import pathlib
from dataclasses import dataclass
from typing import Iterable


@dataclass
class File:
    filepath: pathlib.Path
    # size: int = 0
    dataset: str
    partition: str
    date: dt.date
    extension: str
    # checksum: str = None
    is_most_recent: bool = False


def get_sha1_hash(filepath: pathlib.Path | str) -> str:
    """Returns the SHA1 hash of a file."""
    sha1 = hashlib.sha1()
    with open(filepath, "rb") as f:
        while True:
            data = f.read(65_536)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()


def get_filename(file_info: dict, partition: str, extension: str) -> str:
    """Returns the filename for the given file info and partition."""
    dataset = file_info["dataset"]
    file_datetime = file_info["datetime"].strftime("%Y%m%d")
    match partition:
        case ["year"]:
            year = file_info["year"]
            partition = f"{year}"
        case ["uf", "year"]:
            uf = file_info["uf"].lower()
            year = file_info["year"]
            partition = f"{year}-{uf}"
        case ["uf", "yearmonth"]:
            uf = file_info["uf"].lower()
            year = file_info["year"]
            month = file_info["month"]
            partition = f"{year}{month:02}-{uf}"
        case _:
            partition = ""
    if version := file_info.get("version"):
        partition = partition + f"-{version}"
    filename = "_".join([s for s in (dataset, partition, file_datetime) if s])
    return f"{filename}.{extension}"


def get_file_metadata(file: pathlib.Path) -> File:
    """Returns a dict with the parsed filename."""
    dataset, partition, file_date = file.stem.split("_")
    extension = file.suffix
    file_date = dt.datetime.strptime(file_date, "%Y%m%d").date()
    return File(
        filepath=file,
        # size=file.stat().st_size,
        dataset=dataset,
        partition=partition,
        date=file_date,
        # checksum=get_sha1_hash(file),
        extension=extension,
    )


def get_files_metadata(dirpath: pathlib.Path) -> File:
    files = {}
    for f in dirpath.glob("*.dbc"):
        file = get_file_metadata(f)
        if file.partition not in files:
            files[file.partition] = []
        files[file.partition].append(file)
    for partition in files:
        partition_files_sorted = sorted(
            files[partition],
            key=lambda f: f.filepath.name,
        )
        n_files_partition_sorted = len(partition_files_sorted)
        for i, file in enumerate(partition_files_sorted, 1):
            file.is_most_recent = i == n_files_partition_sorted
            yield file


def get_most_recent(files: Iterable[File]) -> dict[str, File]:
    most_recent_files = [file for file in files if file.is_most_recent]
    return most_recent_files
