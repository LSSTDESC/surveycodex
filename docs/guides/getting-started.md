# Getting started

```python
# The list of available surveys
from galcheat import available_surveys

# Getter methods to retrieve a Survey of a Filter dataclass
from galcheat import get_survey, get_filter

LSST = get_survey("LSST")
u_band = get_filter("u", "LSST")
# which is a proxy for
u_band = LSST.get_filter("u")

# Get the list of available filters
LSST.available_filters

# or as a dictionary with all `Filter` objects
LSST.get_filters()

# Both Survey and Filter classes have physical attributes
LSST.mirror_diameter
u_band.full_exposure_time

# Filters are also attributes of a Survey
LSST.filters.u.full_exposure_time  # same attribute as above

# These attributes are Astropy Quantity objects with units
fwhm = u_band.psf_fwhm
# The value in the original units is obtained as
fwhm.value
# or it can be converted to other units
fwhm.to_value('arcmin')
```
