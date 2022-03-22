r"""

  ____       _  ____ _                _
 / ___| __ _| |/ ___| |__   ___  __ _| |_
| |  _ / _` | | |   | '_ \ / _ \/ _` | __|
| |_| | (_| | | |___| | | |  __/ (_| | |_
 \____|\__,_|_|\____|_| |_|\___|\__,_|\__|

The tiny library of galaxy surveys
most useful parameters with units

The data can be viewed in a terminal with

    python -m galcheat

To access the quantities, retrieve the
`Survey` objects with `get_survey`.

    >>> from galcheat import get_survey
    >>> LSST = get_survey('LSST')
    >>> LSST.mirror_diameter
    <Quantity 8.36 m>

Each `Survey` contains a list of filters
whose names can be obtained as

    >>> LSST.available_filters

Each `Filter` class is accessible through

    >>> u_filter = LSST.get_filter('u')

Parameter values are astropy Quantity objects

    >>> u_filter.psf_fwhm
    <Quantity 0.859 arcsec>
    >>> u_filter.psf_fwhm.value
    0.859
    >>> u_filter.psf_fwhm.unit
    Unit("arcsec")

which can be converted to any physical units
using the `astropy.units` scheme
    >>> u_filter.psf_fwhm.to_value('arcmin')
    0.014316666666666667

Feel free to contribute by submitting
parameter values for your surveys of
interest or reporting inconsistent values.

"""
from galcheat.helpers import available_surveys, get_survey  # noqa
