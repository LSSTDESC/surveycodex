import math

from astropy import units as u
from speclite.filters import ab_reference_flux, load_filter

import galcheat

SPECLITE_SURVEY_PREFIXES = {
    "DES": "decam2014",
    "Euclid_VIS": "Euclid",
    "HSC": "hsc2017",
    "LSST": "lsst2016",
}


def calculate_zero_point(band_name, reference_mag=24):
    """Compute the zeropoint of a given filter with speclite"""
    speclite_filter = load_filter(band_name)
    filter_conv = speclite_filter.convolve_with_function(ab_reference_flux)
    filter_scaled = filter_conv * 10 ** (-0.4 * reference_mag)
    filter_units = filter_scaled.to(1 / (u.s * u.m**2))
    return filter_units


def check_zeropoints(survey_name):
    """
    Compute the zeropoints with speclite and compare with current values

    Parameters
    ----------
    survey_name : str
        Name of the survey

    """
    if survey_name in SPECLITE_SURVEY_PREFIXES.keys():
        survey = galcheat.get_survey(survey_name)
        speclite_prefix = SPECLITE_SURVEY_PREFIXES[survey_name]

        print(f"-- {survey_name} --\t({speclite_prefix} in speclite)\n")
        print("filters |  speclite |  galcheat")
        print("------- | --------- | ---------")

        for filter_name in survey.available_filters:
            if filter_name == "IE":
                old_filter_name = "VIS"
            else:
                old_filter_name = filter_name
            speclite_filter_name = f"{speclite_prefix}-{old_filter_name}"
            zp_24 = (
                calculate_zero_point(speclite_filter_name)
                * survey.effective_area
                * (1 * u.s)
            )
            speclite_zp = (math.log10(zp_24) + 0.4 * 24) / 0.4 * u.mag

            galcheat_filter = survey.get_filter(filter_name)
            current_zp = galcheat_filter.zeropoint
            print(f"{filter_name:^7} | {speclite_zp:.2f} | {current_zp:.2f}")
    else:
        print(f"{survey_name} filters are not available in speclite")
    print("\n")


if __name__ == "__main__":
    print("\nChecking the zeropoints with speclite")
    print("-------------------------------------\n")
    for survey_name in galcheat.available_surveys:
        check_zeropoints(survey_name)
