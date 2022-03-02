from speclite.filters import load_filter

from galcheat import available_surveys, get_survey

speclite_survey_prefixes = {
    "DES": "decam2014-",
    "Euclid_VIS": "Euclid-",
    "HSC": "hsc2017-",
    "Rubin": "lsst2016-",
}


def check_effective_wavelengths(survey_name):
    """Check the current effective wavelengths with speclite
    and compare them to their current values
    """

    if survey_name in speclite_survey_prefixes.keys():
        survey = get_survey(survey_name)
        print(survey_name, ":")

        speclite_prefix = speclite_survey_prefixes[survey_name]

        for filt_name in survey.available_filters:
            speclite_filt_name = f"{speclite_prefix}{filt_name}"
            speclite_filt = load_filter(speclite_filt_name)
            speclite_eff_wl = speclite_filt.effective_wavelength
            current_eff_wl = survey.get_filter(filt_name).effective_wavelength
            print(f"  Filter {filt_name} ({speclite_filt_name} in speclite)")
            print(f"    Speclite effective wavelength: {speclite_eff_wl:.3f}")
            if current_eff_wl is not None:
                print(f"    Current effective wavelength: {current_eff_wl:.3f}")
            else:
                print("    No current value for effective wavelength")
    else:
        print(survey_name, ": filters are not available in speclite")


if __name__ == "__main__":
    for survey_name in available_surveys:
        check_effective_wavelengths(survey_name)
