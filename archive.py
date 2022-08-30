import argparse
import shutil
from pathlib import Path

from datasus_fetcher.storage import File, get_files_metadata


def get_parser():
    parser = argparse.ArgumentParser(
        description="Move old data files to archive",
    )
    parser.add_argument("--datadir", type=Path, required=True)
    parser.add_argument("--archivedatadir", type=Path, required=True)
    parser.add_argument("--extension", required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    datadir = args.datadir
    archivedatadir = args.archivedatadir
    extension = args.extension
    dry_run = args.dry_run
    for datasetdir in datadir.iterdir():
        print(datasetdir)
        datasetname = datasetdir.name
        for datepartitiondir in datasetdir.iterdir():
            files = get_files_metadata(datepartitiondir, extension=extension)
            for file in files:
                file: File
                if not file.is_most_recent:
                    print(file)
                    if dry_run:
                        continue
                    archivedatasetdir: Path = archivedatadir / datasetname
                    archivedatasetdir.mkdir(parents=True, exist_ok=True)
                    archivefilepath = archivedatasetdir / file.filepath.name
                    shutil.move(file.filepath, archivefilepath)


if __name__ == "__main__":
    main()
