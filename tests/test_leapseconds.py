# SPDX-FileCopyrightText: Copyright © 2023 Jamie Nguyen <j@jamielinux.com>
# SPDX-License-Identifier: MIT

from leapseconds import LEAP_SECONDS


def test_leap_seconds():
    assert LEAP_SECONDS[0] == 63072000
