from astropy import units as u
from speclite.filters import load_filter

import surveycodex

SPECLITE_SURVEY_PREFIXES = {
    "DES": "decam2014",
    "Euclid_VIS": "Euclid",
    "Euclid_NISP": "Euclid",
    "HSC": "hsc2017",
    "LSST": "lsst2016",
    "PanSTARRS": "panstarrs",
    "SDSS": "sdss2010",
}

EUCLID_FILTER_NAMES = {"IE": "VIS", "YE": "Y", "JE": "J", "HE": "H"}


def check_effective_wavelengths(survey_name):
    """Compare current effective wavelengths with speclite

    Parameters
    ----------
    survey_name : str
        Name of the survey

    """
    if survey_name in SPECLITE_SURVEY_PREFIXES.keys():
        survey = surveycodex.get_survey(survey_name)
        speclite_prefix = SPECLITE_SURVEY_PREFIXES[survey_name]

        print(f"-- {survey_name} --\t({speclite_prefix} in speclite)\n")
        print("filters |  speclite |  surveycodex")
        print("------- | --------- | ---------")

        for filter_name in survey.available_filters:
            old_filter_name = EUCLID_FILTER_NAMES.get(filter_name, filter_name)
            speclite_filter_name = f"{speclite_prefix}-{old_filter_name}"
            try:
                speclite_filter = load_filter(speclite_filter_name)
            except ValueError as error:
                if str(error).startswith("No such group"):
                    # The speclite version installed in this environment does
                    # not provide this filter group (e.g. older speclite
                    # releases required for Python < 3.10 do not ship all
                    # filter groups).
                    print(
                        f"{speclite_prefix} filter group not available in "
                        "the installed version of speclite"
                    )
                    break
                raise
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
    for survey in surveycodex.available_surveys:
        check_effective_wavelengths(survey)
