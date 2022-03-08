import datetime
import re

from .meta import datasets, states, pattern1, pattern2, pattern3


BASE_PATH = "/dissemin/publicos"


def validate_date(date, date_range):
    today = datetime.date.today()
    if isinstance(date_range[0], tuple):
        year, month = date
        if year < date_range[0][0] or (year == date_range[0][0] and month < date_range[0][1]):
            return False
        if year > today.year or (year == today.year and month > today.month):
            return False
    else:
        if date < date_range[0]:
            return False
        if date > today.year:
            return False
    return True


def get_path(dataset, **kwargs):
    periods = datasets[dataset]["periods"]
    frequency = datasets[dataset]["frequency"]
    if datasets[dataset]["uf"]:
        if "uf" not in kwargs:
            raise ValueError(f"UF is required for dataset {dataset}.")
        elif kwargs["uf"] not in states:
            raise ValueError("UF is invalid")
    for period in periods:
        path_template = period["path"]
        if frequency == "yearly":
            if not validate_date(kwargs["year"], period["date_range"]):
                raise ValueError(f"Invalid year or month for dataset {dataset}.\n{kwargs}")
            if "year_" in path_template:
                kwargs["year_"] = str(kwargs.pop("year"))[2:]
            return BASE_PATH + path_template.format(**kwargs)
        else:
            if not validate_date((kwargs["year"], kwargs["month"]), period["date_range"]):
                raise ValueError(f"Invalid year or month for dataset {dataset}.\n{kwargs}")
            if "year_" in path_template:
                kwargs["year_"] = str(kwargs.pop("year"))[2:]
            return BASE_PATH + path_template.format(**kwargs)


def get_year_filename(year):
    """Returns the filename year."""
    return f"{year}.dbc"


def get_year_month_filename(year, month):
    """Returns the filename yearmonth."""
    return f"{year}{month:02}.dbc"


def get_year_month_uf_filename(year, month, uf):
    """Returns the filename yearmonth-uf."""
    return f"{year}{month:02}-{uf.lower()}.dbc"


def get_year_uf_filename(year, uf):
    """Returns the filename year-uf."""
    return f"{year}-{uf}.dbc"


def get_all_dates(start, end):
    today = datetime.date.today()
    if isinstance(start, tuple):
        if end == (None, None):
            end = (today.year, today.month)
        for year in range(start[0], end[0] + 1):
            for month in range(1, 12 + 1):
                if year == start[0] and month < start[1]:
                    continue
                if year == end[0] and month > end[1]:
                    continue
                yield (year, month)
    else:
        if end is None:
            end = today.year
        for year in range(start, end + 1):
            yield year


def iter_all(dataset):
    periods = datasets[dataset]["periods"]
    frequency = datasets[dataset]["frequency"]
    for period in periods:
        date_range = period["date_range"]
        if frequency == "yearly":
            for year in get_all_dates(date_range[0], date_range[1]):
                if datasets[dataset]["uf"]:
                    for uf in states:
                        yield {
                            "ftp_path": get_path(dataset, year=year, uf=uf),
                            "filename": get_year_uf_filename(year, uf),
                            "date": year,
                            "uf": uf,
                        }
                else:
                    yield {
                        "ftp_path": get_path(dataset, year=year),
                        "filename": get_year_filename(year),
                        "date": year,
                    }
        else:
            for year, month in get_all_dates(date_range[0], date_range[1]):
                if datasets[dataset]["uf"]:
                    for uf in states:
                        yield {
                            "ftp_path": get_path(dataset, year=year, month=month, uf=uf),
                            "filename": get_year_month_uf_filename(year, month, uf),
                            "date": (year, month),
                            "uf": uf,
                        }
                else:
                    yield {
                        "ftp_path": get_path(dataset, year=year, month=month),
                        "filename": get_year_month_filename(year, month),
                        "date": (year, month),
                    }


def parse_filename(filename):
    m1 = re.search(pattern1, filename)
    m2 = re.search(pattern2, filename)
    m3 = re.search(pattern3, filename)
