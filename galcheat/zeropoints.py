import math

from astropy import units as u
from speclite.filters import ab_reference_flux, load_filter

from galcheat.helpers import available_surveys, get_survey

speclite_available_surveys = ["DES", "Euclid_VIS", "HSC", "Rubin"]
speclite_survey_prefixes = ["decam2014-", "Euclid-", "hsc2017-", "lsst2016-"]


def calculate_zero_point(band_name, B0=24):
    """Compute the zeropoint of a given filter with speclite"""
    filt = load_filter(band_name)
    return (filt.convolve_with_function(ab_reference_flux) * 10 ** (-0.4 * B0)).to(
        1 / (u.s * u.m**2)
    )


def check_zeropoints():
    """Recompute the zeropoints with speclite and the effective area
    and compare them to their current values
    """

    for survey_name in available_surveys:
        if survey_name in speclite_available_surveys:
            survey = get_survey(survey_name)
            print(survey_name, ":")

            speclite_prefix = speclite_survey_prefixes[
                speclite_available_surveys.index(survey_name)
            ]

            survey_filters = survey.get_filters()
            for filt_name in survey_filters:
                speclite_filt_name = f"{speclite_prefix}{filt_name}"
                zp_24 = (
                    calculate_zero_point(speclite_filt_name)
                    * survey.effective_area
                    * 1
                    * u.s
                )
                zp_btk = (math.log10(zp_24) + 0.4 * 24) / 0.4

                filt = survey.get_filter(filt_name)
                current_zp = filt.zeropoint
                print(f"  Filter {filt_name} ({speclite_filt_name} in speclite)")
                print(f"    Computed value: {zp_btk:.2f}")
                print(f"    Current value: {current_zp:.2f}")
        else:
            print(survey_name, ": filters are not available in speclite")


if __name__ == "__main__":
    check_zeropoints()
