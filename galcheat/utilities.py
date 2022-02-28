import astropy.units as u

from galcheat.helpers import get_filter, get_survey


def mag2counts(magnitude, survey_name, filter_name):
    """Convert source magnitude to counts for a given filter of a survey

    The calculation includes the effects of atmospheric extinction as
    well as exposure time.

    Parameters
    ----------
    magnitude: float
        magnitude of source
    survey_name: str
        Name of a given survey
    filter_name: str
        Name of the survey filter

    Returns
    -------
    The corresponding flux in counts

    References
    ----------
    The `WeakLensingDeblending` package
    https://github.com/LSSTDESC/WeakLensingDeblending

    """
    if not isinstance(magnitude, u.Quantity):
        magnitude *= u.mag(u.ct / u.s)
    else:
        magnitude = magnitude.value * u.mag(u.ct / u.s)

    filter = get_filter(filter_name, survey_name)

    flux = (magnitude - filter.zeropoint).to(u.ct / u.s)
    counts = flux * filter.exposure_time

    return counts


def mean_sky_level(survey_name, filter_name):
    """Computes the mean sky level for a given survey and a filter

    Parameters
    ----------
    survey_name: str
        Name of a given survey
    filter_name: str
        Name of the survey filter

    Returns
    -------
    The corresponding mean sky level in counts

    """
    survey = get_survey(survey_name)
    filter = get_filter(filter_name, survey_name)

    sky_brightness_counts = mag2counts(filter.sky_brightness, survey_name, filter_name)
    pixel_area = survey.pixel_scale.to_value(u.arcsec) ** 2

    mean_sky_level = sky_brightness_counts * pixel_area

    return mean_sky_level
