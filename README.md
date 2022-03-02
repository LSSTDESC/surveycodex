Galaxy Surveys cheatsheet
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
=========================

[![Python package][gh-workflow-badge]][gh-workflow]
[![License][license-badge]](LICENSE)
![Python supported versions][pyversion-badge]
[![PyPI][pypi-badge]][pypi]

[gh-workflow]: https://github.com/aboucaud/galcheat/actions/workflows/python-package.yml
[gh-workflow-badge]: https://github.com/aboucaud/galcheat/actions/workflows/python-package.yml/badge.svg
[license-badge]: https://img.shields.io/github/license/aboucaud/galcheat?color=blue
[pyversion-badge]: https://img.shields.io/pypi/pyversions/galcheat?color=yellow&logo=pypi
[pypi-badge]: https://badge.fury.io/py/galcheat.svg
[pypi]: https://pypi.org/project/galcheat/


Tiny package containing useful parameters from main galaxy surveys (with units).

The goal of this project is to provide a Python library with minimal dependencies that centralises galaxy survey properties with adequate reference. Such information tends to be scattered in many places or is often copy/pasted without all of the relevant information like units or sources.

**WORK IN PROGRESS: the API is still unstable, expect backward incompatibilities**

[**Getting started**](#getting-started) | [**API**](#api) | [**Contributing**](#contributing) | [**Acknowledgements**](#acknowledgements) | [**License**](#license)

Getting started
---------------
1.  Install the latest version of the library
    ```sh
    pip install -U galcheat
    ```
2. Run the demo = print the available surveys and associated filters
    ```sh
    python -m galcheat
    # or
    galcheat
    ```

API
---
```python
# The list of available surveys
from galcheat import available_surveys

# Getter methods to retrieve a Survey of a Filter dataclass
from galcheat import get_survey, get_filter

Rubin = get_survey("Rubin")
u_band = get_filter("u", "Rubin")
# which is a proxy for
u_band = Rubin.get_filter("u")

# Get the list of available filters
Rubin.available_filters

# or as a dictionary with all `Filter` objects
Rubin.get_filters()

# Both Survey and Filter classes have physical attributes
Rubin.mirror_diameter
u_band.exposure_time

# Filters are also attributes of a Survey
Rubin.filters.u.exposure_time  # same attribute as above

# These attributes are Astropy Quantity objects with units
fwhm = u_band.psf_fwhm
# The value in the original units is obtained as
fwhm.value
# or it can be converted to other units
import astropy.units as u
fwhm.to_value(u.arcmin)
```

Contributing
------------
A number is missing? An error slipped into the files? A survey is not included in the list and you can provide the relevant information or some of it?

Head over to the [contributing guidelines](CONTRIBUTING.md) to learn how to participate into making this library more robust and complete.

The current parameters and the corresponding units are specified in the [data README](galcheat/data/README.md).

Acknowledgements
----------------
This project was started in the context of the [BlendingToolKit (BTK)][github-btk] and [WeakLensingDeblending][github-wld] projects and has initialy received contributions from (alphabetical order)

- Alexandre Boucaud
- Rémy Joseph
- Ismael Mendoza
- Maxime Paillassa
- Thomas Sainrat

[github-wld]: https://github.com/LSSTDESC/WeakLensingDeblending
[github-btk]: https://github.com/LSSTDESC/BlendingToolKit

License
-------
This project is developed under an MIT-license. See [LICENSE file](LICENSE) for more information.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://aboucaud.github.io"><img src="https://avatars.githubusercontent.com/u/3065310?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexandre Boucaud</b></sub></a><br /><a href="https://github.com/aboucaud/galcheat/commits?author=aboucaud" title="Code">💻</a> <a href="#ideas-aboucaud" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-aboucaud" title="Maintenance">🚧</a> <a href="https://github.com/aboucaud/galcheat/pulls?q=is%3Apr+reviewed-by%3Aaboucaud" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/mpaillassa"><img src="https://avatars.githubusercontent.com/u/9745094?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mpaillassa</b></sub></a><br /><a href="https://github.com/aboucaud/galcheat/commits?author=mpaillassa" title="Code">💻</a> <a href="https://github.com/aboucaud/galcheat/pulls?q=is%3Apr+reviewed-by%3Ampaillassa" title="Reviewed Pull Requests">👀</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!