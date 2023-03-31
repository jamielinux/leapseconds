# SPDX-FileCopyrightText: Copyright © 2023 Jamie Nguyen <j@jamielinux.com>
# SPDX-License-Identifier: MIT
# pyright: strict

"""Data for official leap seconds, provided as a tuple of Unix timestamps."""

from typing import Tuple

__all__ = ["LEAP_SECONDS"]

# https://www.ietf.org/timezones/data/leap-seconds.list
LEAP_SECONDS_LIST: Tuple[int, ...] = (
    2272060800,  # 1 Jan 1972
    2287785600,  # 1 Jul 1972
    2303683200,  # 1 Jan 1973
    2335219200,  # 1 Jan 1974
    2366755200,  # 1 Jan 1975
    2398291200,  # 1 Jan 1976
    2429913600,  # 1 Jan 1977
    2461449600,  # 1 Jan 1978
    2492985600,  # 1 Jan 1979
    2524521600,  # 1 Jan 1980
    2571782400,  # 1 Jul 1981
    2603318400,  # 1 Jul 1982
    2634854400,  # 1 Jul 1983
    2698012800,  # 1 Jul 1985
    2776982400,  # 1 Jan 1988
    2840140800,  # 1 Jan 1990
    2871676800,  # 1 Jan 1991
    2918937600,  # 1 Jul 1992
    2950473600,  # 1 Jul 1993
    2982009600,  # 1 Jul 1994
    3029443200,  # 1 Jan 1996
    3076704000,  # 1 Jul 1997
    3124137600,  # 1 Jan 1999
    3345062400,  # 1 Jan 2006
    3439756800,  # 1 Jan 2009
    3550089600,  # 1 Jul 2012
    3644697600,  # 1 Jul 2015
    3692217600,  # 1 Jan 2017
)

# The published timestamps count from 1st Jan 1900.
# Unix timestamps count from 1st Jan 1970.
# The difference between these dates is 2,208,988,800 seconds.
LEAP_SECONDS: Tuple[int, ...] = tuple(x - 2208988800 for x in LEAP_SECONDS_LIST)
