import astropy.units as u

from galcheat.filter import Filter
from galcheat.helpers import get_survey
from galcheat.survey import Survey


def mag2counts(magnitude, survey, filter, exposure_time=None):
    """Convert source magnitude to electron counts for a given survey filter

    To perform the computation, we use the filter zeropoint computed
    with `speclite` at a given airmass under classical atmospheric
    conditions and by default integrated over the survey lifetime.

    An exposure time can be provided to compute the corresponding counts
    instead of the full filter exposure time.

    Expect a rough estimate from this calculation since e.g. it does not
    take into account the atmospheric extinction. Therefore the result
    is cast to an integer.

    Parameters
    ----------
    magnitude: float
        magnitude of source
    survey: str or Survey
        Name of a given survey or Survey instance
    filter: str or Filter
        Name of the survey filter or Filter instance
    exposure_time: float or Quantity[float] (optional)
        Exposure time of the filter in seconds.
        If not provided, the full filter exposure time is used.

    Returns
    -------
    Quantity[int]
        The corresponding flux in electron counts

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
        magnitude *= u.mag(u.electron / u.s)
    else:
        magnitude = magnitude.value * u.mag(u.electron / u.s)

    if not isinstance(survey, Survey):
        survey = get_survey(survey)

    if not isinstance(filter, Filter):
        filter = survey.get_filter(filter)

    flux = (magnitude - filter.zeropoint).to(u.electron / u.s)

    exposure_time = exposure_time or filter.full_exposure_time
    if not isinstance(exposure_time, u.Quantity):
        exposure_time *= u.s

    counts = flux * exposure_time

    return counts.astype(int)


def mean_sky_level(survey, filter):
    """Computes the mean sky level for a given survey and a filter

    This computation uses the sky brightness parameter from galcheat,
    expressed as a magnitude per sky area, weights it by the
    pixel area and converts it to electron counts.

    Parameters
    ----------
    survey: str or Survey
        Name of a given survey or Survey instance
    filter: str or Filter
        Name of the survey filter of Filter instance

    Returns
    -------
    Quantity[float]
        The corresponding mean sky level in electron counts

    Example
    -------
    >>> from galcheat.utilities import mean_sky_level
    >>> mean_sky_level("LSST", "g")
    <Quantity 23241.84 ct>

    """
    if not isinstance(survey, Survey):
        survey = get_survey(survey)

    if not isinstance(filter, Filter):
        filter = survey.get_filter(filter)

    sky_brightness_counts = mag2counts(filter.sky_brightness, survey, filter)
    pixel_area = survey.pixel_scale.to_value(u.arcsec) ** 2

    mean_sky_level = sky_brightness_counts * pixel_area

    return mean_sky_level
