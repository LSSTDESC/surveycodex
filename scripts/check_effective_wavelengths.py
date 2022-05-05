from astropy import units as u
from speclite.filters import load_filter

import galcheat

SPECLITE_SURVEY_PREFIXES = {
    "DES": "decam2014",
    "Euclid_VIS": "Euclid",
    "HSC": "hsc2017",
    "LSST": "lsst2016",
}


def check_effective_wavelengths(survey_name):
    """Compare current effective wavelengths with speclite

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
            speclite_filter = load_filter(speclite_filter_name)
            speclite_eff_wl = speclite_filter.effective_wavelength.to(u.nm)
            current_eff_wl = survey.get_filter(filter_name).effective_wavelength

            if current_eff_wl is None:
                print(f"{filter_name:^7} | {speclite_eff_wl:.2f} | {current_eff_wl:^9}")
            else:
                print(
                    f"{filter_name:^7} | {speclite_eff_wl:.2f} | {current_eff_wl:.2f}"
                )
    else:
        print(f"{survey_name} filters are not available in speclite")
    print("\n")


if __name__ == "__main__":
    print("\nChecking the effective filter wavelengths with speclite")
    print("-------------------------------------------------------\n")
    for survey in galcheat.available_surveys:
        check_effective_wavelengths(survey)
