Galaxy Surveys cheatsheet
=========================

[![Python package][gh-workflow-badge]][gh-workflow]
[![License][license-badge]](LICENSE)
[![PyPI][pypi-badge]][pypi]

[gh-workflow]: https://github.com/aboucaud/galcheat/actions/workflows/python-package.yml
[gh-workflow-badge]: https://github.com/aboucaud/galcheat/actions/workflows/python-package.yml/badge.svg
[license-badge]: https://img.shields.io/github/license/aboucaud/galcheat?color=blue
[pypi-badge]: https://img.shields.io/pypi/pyversions/galcheat?color=yellow&logo=pypi
[pypi]: https://pypi.org/project/galcheat/


Tiny package containing useful parameters from main galaxy surveys (with units)

The goal of this project is to provide a centralised library containing galaxy survey properties often required for simulations. Such information tends to be scattered in many places or is often copy/pasted without all of the relevant information like units or sources.

**WORK IN PROGRESS**

[**Setup**](#setup) | [**API**](#api) | [**Acknowledgements**](#acknowledgements) | [**License**](#license)

Setup
-----
1. Create and activate a virtual environment (optional)
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
2.  Install the library with its requirements
    ```sh
    python -m pip install galcheat
    ```
3. Run the demo = print the available surveys and associated filters
    ```sh
    python -m galcheat
    # or
    galcheat
    ```

API
---
```python
from galcheat import survey_info

# Available surveys
print(list(survey_info.keys()))

# Rubin U band PSF FWHM
Rubin = survey_info["Rubin"]
fwhm = Rubin.filters.u.psf_fwhm  # Quantity object with units
print(fwhm)

# Retrieve the value in the original units
print(fwhm.value)

# Or convert to other units
import astropy.units as u
print(fwhm.to_value(u.arcmin))
```

Acknowledgements
----------------
This project was started in the context of the [BlendingToolKit (BTK)][github-btk] and has initialy received contributions from (alphabetical order)

- Alexandre Boucaud
- Rémy Joseph
- Ismael Mendoza
- Maxime Paillassa
- Thomas Sainrat

[github-btk]: https://github.com/LSSTDESC/BlendingToolKit

License
-------
This project is developed under an MIT-license. See [LICENSE file](LICENSE) for more information.
