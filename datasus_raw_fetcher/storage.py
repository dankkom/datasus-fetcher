import hashlib
import pathlib

from . import meta


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


def get_filename(file_info: dict, partition: str) -> str:
    """Returns the filename for the given file info and partition."""
    file_datetime = file_info["datetime"].strftime("%Y%m%d")
    match partition:
        case "year":
            year = file_info["year"]
            return f"{year}_{file_datetime}.dbc"
        case "uf-year":
            uf = file_info["uf"]
            year = file_info["year"]
            return f"{year}-{uf}_{file_datetime}.dbc"
        case "uf-yearmonth":
            uf = file_info["uf"]
            year = file_info["year"]
            month = file_info["month"]
            return f"{year}{month:02}-{uf.lower()}_{file_datetime}.dbc"
