r"""

  ____       _  ____ _                _
 / ___| __ _| |/ ___| |__   ___  __ _| |_
| |  _ / _` | | |   | '_ \ / _ \/ _` | __|
| |_| | (_| | | |___| | | |  __/ (_| | |_
 \____|\__,_|_|\____|_| |_|\___|\__,_|\__|

The tiny library of galaxy surveys
most useful parameters (with units)

The data can be viewed in a terminal with

    python -m galcheat

To access the quantities, use the main
dictionary called `survey_info` containing
`Survey` objects

    >>> from galcheat import survey_info
    >>> Rubin = survey_info['Rubin']
    >>> Rubin.mirror_diameter
    <Quantity 8.36 m>

Each `Survey` contains its own `Filter` list
accessible from the `Survey`

    >>> u_filter = Rubin.filters.u

or as an ordered list

    >>> filters = Rubin.get_filters()
    >>> u_filter = filters[0]

And parameter values can be converted to any
physical units using the `astropy.units` scheme

    >>> u_filter.psf_fwhm
    <Quantity 0.859 arcsec>
    >>> u_filter.value
    0.859

    >>> from astropy import units as u
    >>> u_filter.psf_fwhm.to(u.arcmin).value
or
    >>> u_filter.psf_fwhm.to_value(u.arcmin)
    0.014316666666666667

Feel free to contribute by submitting
parameter values for your surveys of
interest or reporting unconsitent
values.

"""
from pathlib import Path

from galcheat.survey import Survey

_BASEDIR = Path(__file__).parent.resolve()

survey_info = {
    path.stem: Survey.from_yaml(path) for path in _BASEDIR.glob("data/*.yaml")
}
