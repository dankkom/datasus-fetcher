import argparse
import pathlib

from datasus_raw_fetcher import fetcher, meta


def download(datasets, destdir):
    ftp = fetcher.connect()
    if datasets:
        datasets_ = set(datasets) & set(meta.datasets.keys())
    else:
        datasets_ = meta.datasets.keys()
    for dataset in datasets_:
        fetcher.download_dataset(ftp, dataset, destdir)
    ftp.close()


def get_parser():
    parser = argparse.ArgumentParser(
        description="Download all raw files from datasus",
    )
    parser.add_argument(
        "datasets",
        nargs="*",
        help="Datasets to download",
    )
    parser.add_argument(
        "destdir",
        type=pathlib.Path,
        help="Directory to download to",
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    datasets = args.datasets
    destdir = args.destdir
    download(datasets, destdir)


if __name__ == "__main__":
    main()
