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

To access the quantities, retrieve the
`Survey` objects with `get_survey`.

    >>> from galcheat import get_survey
    >>> Rubin = get_survey('Rubin')
    >>> Rubin.mirror_diameter
    <Quantity 8.36 m>

Each `Survey` contains its own `Filter` list
accessible from the `Survey`

    >>> u_filter = Rubin.filters.u

or as a dictionary

    >>> filters = Rubin.get_filters()
    >>> u_filter = filters['u']

And parameter values can be converted to any
physical units using the `astropy.units` scheme

    >>> u_filter.psf_fwhm
    <Quantity 0.859 arcsec>
    >>> u_filter.value
    0.859

    >>> import astropy.units as u
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
_survey_info = {
    path.stem: Survey.from_yaml(path) for path in _BASEDIR.glob("data/*.yaml")
}

available_surveys = list(_survey_info.keys())


def get_survey(survey_name: str):
    """Get the dataclass corresponding to the survey

    Raises
    ------
    ValueError: when the input survey is not (currently) available

    """
    if survey_name not in available_surveys:
        raise ValueError(
            "Please check the survey name. "
            f"The available surveys are {available_surveys}"
        )

    return _survey_info[survey_name]


def get_filter(filter_name: str, survey: Survey):
    """
    Parameters
    ----------
    filter_name: str
        Name of a filter


    Returns
    -------
    a filter dataclass

    Raises
    ------
    ValueError: when the input filter is not available

    """
    filter_dict = survey.get_filters()
    available_filters = list(filter_dict.keys())

    if filter_name not in available_filters:
        raise ValueError(
            "Please check the filter name. "
            f"The available filters for {survey.name} "
            f"are {available_filters}"
        )

    return filter_dict[filter_name]
