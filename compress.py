import argparse
import pathlib
import subprocess

from datasus_fetcher import meta


def compress_files_by_period(dataset_dirpath: pathlib.Path, destdirpath: pathlib.Path):
    dataset = dataset_dirpath.name
    periods = set(
        [
            partition.split("-")[0]
            for _, partition, _ in (
                f.stem.split("_")
                for f in dataset_dirpath.iterdir()
            )
        ]
    )
    for period in sorted(periods):
        dest_filepath = destdirpath / f"{dataset}_{period}.7z"
        if dest_filepath.exists():
            continue
        if not dest_filepath.parent.exists():
            dest_filepath.parent.mkdir(parents=True)
        cmd = [
            "7z",
            "a",
            "-t7z",
            "-m0=lzma2",
            str(dest_filepath),
            f"{dataset_dirpath}/{dataset}_{period}*.dbc",
        ]
        print(cmd)
        subprocess.run(cmd)


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compress all raw files in the given directory"
    )
    parser.add_argument(
        "dirpath",
        type=pathlib.Path,
        help="Directory to compress",
    )
    parser.add_argument(
        "destdirpath",
        type=pathlib.Path,
        help="Directory to store compressed files",
    )
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    dirpath = args.dirpath
    destdirpath = args.destdirpath
    for dataset in meta.datasets:
        if not (dirpath / dataset).exists():
            continue
        compress_files_by_period(dirpath / dataset, destdirpath / dataset)
