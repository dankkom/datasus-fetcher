import argparse
import pathlib

from datasus_raw_fetcher import fetcher, meta


def download(destdir):
    ftp = fetcher.connect()

    for dataset in meta.datasets:
        fetcher.download_dataset(ftp, dataset, destdir)

    ftp.close()


def get_parser():
    parser = argparse.ArgumentParser(
        description="Download all raw files from datasus"
    )
    parser.add_argument(
        "destdir", type=pathlib.Path, help="Directory to download to"
    )
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    destdir = args.destdir
    download(destdir)
