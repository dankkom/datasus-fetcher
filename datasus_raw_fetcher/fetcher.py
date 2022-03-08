import datetime as dt
import ftplib
import pathlib

from .utils import get_sha1_hash

FTP_HOST = "ftp.datasus.gov.br"


def connect():
    """Connects to the FTP server."""
    ftp = ftplib.FTP(FTP_HOST, encoding="latin-1")
    ftp.login()
    return ftp


def list_files(ftp):
    """List all files in the current directory."""
    files = []
    ftp.retrlines("LIST", files.append)
    # parse files' date, size and name
    files = [
        {
            "datetime": dt.datetime.strptime(date + " " + time, "%m-%d-%y %I:%M%p"),
            "size": int(size),
            "name": name,
        }
        for date, time, size, name in map(str.split, files)
    ]
    return files


def fetch_file(path, dest_filepath, ftp):
    """Fetch a file from a remote FTP server.

    :param path: The path to the file.
    :param dest_filepath: The destination file path.
    :param ftp: The FTP connection.
    """

    if isinstance(dest_filepath, str):
        dest_filepath = pathlib.Path(dest_filepath.lower())
    if not dest_filepath.parent.exists():
        dest_filepath.parent.mkdir(parents=True)

    try:
        with open(dest_filepath, "wb") as f:
            ftp.retrbinary("RETR " + path, f.write)
        sha1 = get_sha1_hash(dest_filepath)
        return sha1
    except ftplib.error_perm:
        print(f"File {path} not found.")
        dest_filepath.unlink()
