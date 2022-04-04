import hashlib
import pathlib


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
        case "year":
            year = file_info["year"]
            return f"{dataset}_{year}_{file_datetime}.{extension}"
        case "uf-year":
            uf = file_info["uf"]
            year = file_info["year"]
            return f"{dataset}_{year}-{uf}_{file_datetime}.{extension}"
        case "uf-yearmonth":
            uf = file_info["uf"]
            year = file_info["year"]
            month = file_info["month"]
            return f"{dataset}_{year}{month:02}-{uf.lower()}_{file_datetime}.{extension}"
