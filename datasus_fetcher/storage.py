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
            partition = f"{year}"
        case "uf-year":
            uf = file_info["uf"].lower()
            year = file_info["year"]
            partition = f"{year}-{uf}"
        case "uf-yearmonth":
            uf = file_info["uf"].lower()
            year = file_info["year"]
            month = file_info["month"]
            partition = f"{year}{month:02}-{uf}"
    return f"{dataset}_{partition}_{file_datetime}.{extension}"
