Galaxy Surveys cheatsheet
=========================

**WORK IN PROGRESS**

API
---
```python
from galcheat import survey_info

Rubin = survey_info["Rubin"]

# U band PSF FWHM
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
    git clone https://github.com/aboucaud/galcheat
    ```
2. create a virtual environment and install the requirements
    ```
    python -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    ```
3. run the demo (currently only with Rubin data)
    ```
    python -m galcheat
    ```
