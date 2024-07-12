[**Main documentation**](https://aboucaud.github.io/galcheat/) | [**Getting started**](#getting-started) | [**CLI**](#cli) | [**API**](#api) | [**Contributing**](#contributing) | [**License**](#license)

<!-- <br>
<img src="docs/images/surveycodex_logo.png" alt="surveycodex" height=200px>
</p> -->

# SurveyCodex

[![Python package][gh-workflow-badge]][gh-workflow]
[![License][license-badge]](LICENSE)
![Python supported versions][pyversion-badge]
[![PyPI][pypi-badge]][pypi]<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[gh-workflow]: https://github.com/LSSTDESC/surveycodex/actions/workflows/python-package.yml
[gh-workflow-badge]: https://github.com/LSSTDESC/surveycodex/actions/workflows/python-package.yml/badge.svg
[license-badge]: https://img.shields.io/github/license/LSSTDESC/surveycodex?color=blue
[pyversion-badge]: https://img.shields.io/pypi/pyversions/surveycodex?color=yellow&logo=pypi
[pypi-badge]: https://badge.fury.io/py/surveycodex.svg
[pypi]: https://pypi.org/project/surveycodex/

Tiny package containing useful parameters from main galaxy surveys (**with units**).

The goal of this project is to provide a Python library with minimal dependencies that centralises galaxy survey properties with adequate reference. Such information tends to be scattered in many places or is often copy/pasted without all of the relevant information like units or sources.

The current parameters and the corresponding units are specified in the [documentation](https://aboucaud.github.io/galcheat/parameters.html)

Getting started
---------------
Install the latest version of the library
```sh
pip install -U surveycodex
```

CLI
---

Print the available surveys and associated filters

```sh
surveycodex
```

### Options
- **`-s <survey>`**: print information for a given survey
- **`--refs`**: print the source for each parameter
- **`--rich`**: use pretty printing for the terminal (needs the `rich` library installed)
- **`-h, --help`**: get help

### Examples
```sh
surveycodex -s LSST         # LSST info
surveycodex --refs          # all surveys info with refs
surveycodex --refs -s HSC   # HSC info with refs
surveycodex -s LSST --rich  # pretty print rich terminal output for LSST info
```

API
---
```python
import surveycodex

# Start with the list of available surveys
surveycodex.available_surveys

# Retrieve a Survey instance
LSST = surveycodex.get_survey("LSST")

# List the available survey filters
LSST.available_filters

# Pick a Filter instance
u_band = LSST.get_filter("u")

# Both Survey and Filter objects have physical attributes
LSST.mirror_diameter

u_band.full_exposure_time

# These attributes are Astropy Quantity objects
# whose value can be retrieved in any desired unit
u_band.psf_fwhm.to_value('arcmin')
```

## Contributing ✨

This project was started in the context of the [BlendingToolKit (BTK)][github-btk] and [WeakLensingDeblending][github-wld] projects and has received contributions from these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://aboucaud.github.io"><img src="https://avatars.githubusercontent.com/u/3065310?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexandre Boucaud</b></sub></a><br /><a href="https://github.com/LSSTDESC/surveycodex/commits?author=aboucaud" title="Code">💻</a> <a href="#ideas-aboucaud" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-aboucaud" title="Maintenance">🚧</a> <a href="https://github.com/LSSTDESC/surveycodex/pulls?q=is%3Apr+reviewed-by%3ALSSTDESC" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/mpaillassa"><img src="https://avatars.githubusercontent.com/u/9745094?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mpaillassa</b></sub></a><br /><a href="https://github.com/LSSTDESC/surveycodex/commits?author=mpaillassa" title="Code">💻</a> <a href="https://github.com/LSSTDESC/surveycodex/pulls?q=is%3Apr+reviewed-by%3Ampaillassa" title="Reviewed Pull Requests">👀</a> <a href="#data-mpaillassa" title="Data">🔣</a></td>
    <td align="center"><a href="https://ismael-mendoza.github.io/"><img src="https://avatars.githubusercontent.com/u/11745764?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ismael Mendoza</b></sub></a><br /><a href="#ideas-ismael-mendoza" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LSSTDESC/surveycodex/pulls?q=is%3Apr+reviewed-by%3Aismael-mendoza" title="Reviewed Pull Requests">👀</a> <a href="#data-ismael-mendoza" title="Data">🔣</a></td>
    <td align="center"><a href="https://github.com/HironaoMiyatake"><img src="https://avatars.githubusercontent.com/u/1507529?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hironao Miyatake</b></sub></a><br /><a href="https://github.com/LSSTDESC/surveycodex/commits?author=HironaoMiyatake" title="Code">💻</a> <a href="#data-HironaoMiyatake" title="Data">🔣</a></td>
    <td align="center"><a href="https://github.com/aguinot"><img src="https://avatars.githubusercontent.com/u/39480528?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Axel Guinot</b></sub></a><br /><a href="#data-aguinot" title="Data">🔣</a></td>
    <td align="center"><a href="https://github.com/thuiop"><img src="https://avatars.githubusercontent.com/u/1338337?v=4?s=100" width="100px;" alt=""/><br /><sub><b>thuiop</b></sub></a><br /><a href="#ideas-thuiop" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://remyjoseph.wordpress.com/"><img src="https://avatars.githubusercontent.com/u/16084926?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rémy Joseph</b></sub></a><br /><a href="#ideas-herjy" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.

A number is missing? An error slipped into the files? A survey is not included in the list and you can provide the relevant information or some of it?

Contributions of any kind are welcome! Head over to the [contributing guidelines](CONTRIBUTING.md) to learn how to participate into making this library more robust and complete.

[github-wld]: https://github.com/LSSTDESC/WeakLensingDeblending
[github-btk]: https://github.com/LSSTDESC/BlendingToolKit

License
-------
This project is developed under an MIT-license. See [LICENSE file](LICENSE) for more information.
