import astropy.units as u

from galcheat.helpers import get_filter, get_survey


def mag2counts(magnitude, survey_name, filter_name):
    """Convert source magnitude to counts for a given filter of a survey

    To perform the computation, we use the filter zeropoint computed
    with `speclite` under classical atmospheric conditions and at a
    given airmass and we integrate over the survey lifetime using the
    full filter exposure time.

    Expect a rough estimate from this calculation since e.g. it does not
    take into account the atmospheric extinction. Therefore the result
    is casted to an integer.

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
    Quantity[int]
        The corresponding flux in counts

    Example
    -------
    >>> from galcheat.utilities import mag2counts
    >>> mag2counts(24, "LSST", "g")
    <Quantity 121397 ct>

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

    return counts.astype(int)


def mean_sky_level(survey_name, filter_name):
    """Computes the mean sky level for a given survey and a filter

    This computation uses the sky brightness parameter from galcheat,
    expressed as a magnitude per square arcminute, weights it by the
    pixel area and converts it to counts.

    Parameters
    ----------
    survey_name: str
        Name of a given survey
    filter_name: str
        Name of the survey filter

    Returns
    -------
    Quantity[float]
        The corresponding mean sky level in counts

    Example
    -------
    >>> from galcheat.utilities import mean_sky_level
    >>> mean_sky_level("LSST", "g")
    <Quantity 23241.84 ct>

    """
    survey = get_survey(survey_name)
    filter = get_filter(filter_name, survey_name)

    sky_brightness_counts = mag2counts(filter.sky_brightness, survey_name, filter_name)
    pixel_area = survey.pixel_scale.to_value(u.arcsec) ** 2

    mean_sky_level = sky_brightness_counts * pixel_area

    return mean_sky_level
