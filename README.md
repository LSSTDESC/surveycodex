Galaxy Surveys cheatsheet
=========================

Tiny package containing useful parameters from main galaxy surveys (with units)

The goal of this project is to provide a centralised library containing galaxy survey properties often required for simulations. Such information tends to be scattered in many places or is often copy/pasted without all of the relevant information like units or sources.

**WORK IN PROGRESS**

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

Demo
----
1. clone the project
    ```
    git clone https://github.com/aboucaud/galcheat && cd galcheat
    ```
2. create a virtual environment and install the requirements
    ```
    python -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    ```
3. run the demo = print the available surveys and associated filters
    ```
    python -m galcheat
    ```
