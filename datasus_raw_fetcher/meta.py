# Brazil UFs
states = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
]

uf_pattern = r"(ac|al|ap|am|ba|ce|df|es|go|ma|mt|ms|mg|pa|pb|pr|pe|pi|rj|rn|rs|ro|rr|sc|sp|se|to)"
monthly_pattern = r"(9|0|1|2)\d(0|1)\d"  # 9701
year_4digit_pattern = r"(19|20)\d{2}"    # 1997
year_2digit_pattern = r"\d{2}"           # 97
pattern1 = r"{uf}{monthly}\.dbc$".format(uf=uf_pattern, monthly=monthly_pattern)
pattern2 = r"{yearly}\.dbc$".format(yearly=year_4digit_pattern)
pattern3 = r"{yearly}\.dbc$".format(yearly=year_2digit_pattern)
pattern4 = r"{uf}{yearly}\.dbc$".format(uf=uf_pattern, yearly=year_4digit_pattern)
pattern5 = r"{uf}{yearly}\.dbc$".format(uf=uf_pattern, yearly=year_2digit_pattern)


datasets = {
    "sih-rd": {
        "periods": [
            {
                "path": "/SIHSUS/199201_200712/Dados/RD{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^rd" + pattern1,
                "date_range": ((1992, 1), (2007, 12)),
            },
            {
                "path": "/SIHSUS/200801_/Dados/RD{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^rd" + pattern1,
                "date_range": ((2008, 1), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "sih-rj": {
        "periods": [
            {
                "path": "/SIHSUS/200801_/Dados/RJ{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^rj" + pattern1,
                "date_range": ((2008, 1), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "sih-sp": {
        "periods": [
            {
                "path": "/SIHSUS/199201_200712/Dados/SP{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^sp" + pattern1,
                "date_range": ((1997, 1), (2007, 12)),
            },
            {
                "path": "/SIHSUS/200801_/Dados/SP{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^sp" + pattern1,
                "date_range": ((2008, 1), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "sih-er": {
        "periods": [
            {
                "path": "/SIHSUS/200801_/Dados/ER{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^er" + pattern1,
                "date_range": ((2011, 1), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "sinasc": {
        "periods": [
            {
                "path": "/SINASC/1994_1995/Dados/DNRES/DNR{uf}{year}.dbc",
                "filename_pattern": r"^dnr" + pattern4,
                "date_range": (1994, 1995),
            },
            {
                "path": "/SINASC/1996_/Dados/DNRES/DN{uf}{year}.dbc",
                "filename_pattern": r"^dn" + pattern4,
                "date_range": (1996, None),
            }
        ],
        "frequency": "yearly",
        "uf": True,
    },
    "sim-do": {
        "periods": [
            {
                "path": "/SIM/CID9/DORES/DOR{uf}{year_:02}.dbc",
                "filename_pattern": r"^dor" + pattern5,
                "date_range": (1979, 1995),
            },
            {
                "path": "/SIM/CID10/DORES/DO{uf}{year}.dbc",
                "filename_pattern": r"^do" + pattern4,
                "date_range": (1996, None),
            }
        ],
        "frequency": "yearly",
        "uf": True,
    },
    "sim-doext": {
        "periods": [
            {
                "path": "/SIM/CID9/DOFET/DOEXT{year_:02}.dbc",
                "filename_pattern": r"^doext" + pattern3,
                "date_range": (1979, 1995),
            },
            {
                "path": "/SIM/CID10/DOFET/DOEXT{year_:02}.dbc",
                "filename_pattern": r"^doext" + pattern3,
                "date_range": (1996, None),
            }
        ],
        "frequency": "yearly",
        "uf": False,
    },
    "sim-dofet": {
        "periods": [
            {
                "path": "/SIM/CID9/DOFET/DOFET{year_:02}.dbc",
                "filename_pattern": r"^dofet" + pattern3,
                "date_range": (1979, 1995),
            },
            {
                "path": "/SIM/CID10/DOFET/DOFET{year}.dbc",
                "filename_pattern": r"^dofet" + pattern2,
                "date_range": (1996, None),
            }
        ],
        "frequency": "yearly",
        "uf": False,
    },
    "sim-doinf": {
        "periods": [
            {
                "path": "/SIM/CID9/DOFET/DOINF{year_:02}.dbc",
                "filename_pattern": r"^doinf" + pattern3,
                "date_range": (1979, 1995),
            },
            {
                "path": "/SIM/CID10/DOFET/DOINF{year_:02}.dbc",
                "filename_pattern": r"^doinf" + pattern3,
                "date_range": (1996, None),
            },
        ],
        "frequency": "yearly",
        "uf": False,
    },
    "sim-domat": {
        "periods": [
            {
                "path": "/SIM/CID10/DOFET/DOMAT{year_:02}.dbc",
                "filename_pattern": r"^domat" + pattern3,
                "date_range": (1996, None),
            },
        ],
        "frequency": "yearly",
        "uf": False,
    },
    "cnes-dc": {
        "periods": [
            {
                "path": "/200508_/Dados/DC/DC{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^dc" + pattern1,
                "date_range": ((2005, 8), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-ee": {
        "periods": [
            {
                "path": "/200508_/Dados/EE/EE{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^ee" + pattern1,
                "date_range": ((2007, 3), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-ef": {
        "periods": [
            {
                "path": "/200508_/Dados/EF/EF{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^ef" + pattern1,
                "date_range": ((2007, 3), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-ep": {
        "periods": [
            {
                "path": "/200508_/Dados/EP/EP{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^ep" + pattern1,
                "date_range": ((2007, 4), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-eq": {
        "periods": [
            {
                "path": "/200508_/Dados/EQ/EQ{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^eq" + pattern1,
                "date_range": ((2005, 8), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-gm": {
        "periods": [
            {
                "path": "/200508_/Dados/GM/GM{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^gm" + pattern1,
                "date_range": ((2007, 7), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-hb": {
        "periods": [
            {
                "path": "/200508_/Dados/HB/HB{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^hb" + pattern1,
                "date_range": ((2007, 3), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
    "cnes-in": {
        "periods": [
            {
                "path": "/200508_/Dados/IN/IN{uf}{year_:02}{month:02}.dbc",
                "filename_pattern": r"^in" + pattern1,
                "date_range": ((2007, 11), (None, None)),
            },
        ],
        "frequency": "monthly",
        "uf": True,
    },
}
