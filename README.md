# leapseconds

[![PyPi Version][pypi-img]][pypi-url]
[![License][license-img]][license-url]
[![Continuous Integration][ci-img]][ci-url]
[![Code Coverage][coverage-img]][coverage-url]
[![Python Versions][python-img]][python-url]

[pypi-img]: https://img.shields.io/pypi/v/leapseconds.svg
[pypi-url]: https://pypi.org/project/leapseconds
[license-img]:  https://img.shields.io/github/license/jamielinux/leapseconds.svg
[license-url]: https://github.com/jamielinux/leapseconds/blob/main/LICENSE
[ci-img]: https://github.com/jamielinux/leapseconds/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/jamielinux/leapseconds/actions/workflows/ci.yml
[coverage-img]: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jamielinux/7c0026bdbd4a00863dcd6878e5e3b943/raw/leapseconds.covbadge.json
[coverage-url]: https://github.com/jamielinux/leapseconds/actions/workflows/ci.yml
[python-img]: https://img.shields.io/pypi/pyversions/leapseconds.svg
[python-url]: https://pypi.org/project/leapseconds

---

**leapseconds** is a Python library with data on official leap seconds, provided as a
tuple of Unix timestamps.

Source data: [https://www.ietf.org/timezones/data/leap-seconds.list][0]

[0]: https://www.ietf.org/timezones/data/leap-seconds.list

## Installation

```console
pip install leapseconds
```

## Usage

```python
from leapseconds import LEAP_SECONDS

# Check if a Unix timestamp represents an officially announced leap second:
if 63072000 in LEAP_SECONDS:
    print("True")
```

- **`LEAP_SECONDS`**:
  - A `tuple` of Unix timestamps (`int`) that represent officially announced leap
    seconds in chronological order.

## License

`leapseconds` is distributed under the terms of the [MIT][license] license.

[license]: https://spdx.org/licenses/MIT.html
