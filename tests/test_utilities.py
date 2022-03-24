import pytest

from galcheat.helpers import get_survey
from galcheat.utilities import mag2counts, mean_sky_level

BTK_COUNTS_MAG24 = {
    "LSST_u": 15321.782101179268,
    "LSST_g": 121397.91888074754,
    "LSST_r": 240956.73939657194,
    "LSST_i": 179448.18815675998,
    "LSST_z": 108953.51289042353,
    "LSST_y": 50727.240442255556,
}

MEAN_SKY_LEVEL = {
    "LSST_u": 1553,
    "LSST_g": 24114,
    "LSST_r": 127057,
    "LSST_i": 183653,
    "LSST_z": 250784,
    "LSST_y": 290603,
}


@pytest.fixture(
    params=[("LSST", f) for f in "ugrizy"], ids=lambda x: f"survey:{x[0]}-filter:{x[1]}"
)
def lsst_btk_counts(request):
    survey, filt = request.param
    expected = int(BTK_COUNTS_MAG24[f"{survey}_{filt}"])
    return survey, filt, expected


@pytest.fixture(
    params=[("LSST", f) for f in "ugrizy"], ids=lambda x: f"survey:{x[0]}-filter:{x[1]}"
)
def lsst_btk_sky_level(request):
    survey, filt = request.param
    expected = int(MEAN_SKY_LEVEL[f"{survey}_{filt}"])
    return survey, filt, expected


def test_mag2counts_str(lsst_btk_counts):
    survey, filt, expected = lsst_btk_counts
    assert mag2counts(24, survey, filt).value == expected


def test_mag2counts_filter_str(lsst_btk_counts):
    survey, filt, expected = lsst_btk_counts
    survey_inst = get_survey(survey)
    assert mag2counts(24, survey_inst, filt).value == expected


def test_mag2counts_filter_instance(lsst_btk_counts):
    survey, filt, expected = lsst_btk_counts
    survey_inst = get_survey(survey)
    filt_inst = survey_inst.get_filter(filt)
    assert mag2counts(24, survey_inst, filt_inst).value == expected


def test_mean_sky_level_str(lsst_btk_sky_level):
    survey, filt, expected = lsst_btk_sky_level
    sky_level = mean_sky_level(survey, filt).value
    assert int(sky_level) == expected


def test_mean_sky_level_filter_str(lsst_btk_sky_level):
    survey, filt, expected = lsst_btk_sky_level
    survey_inst = get_survey(survey)
    sky_level = mean_sky_level(survey_inst, filt).value
    assert int(sky_level) == expected


def test_mean_sky_level_filter_instance(lsst_btk_sky_level):
    survey, filt, expected = lsst_btk_sky_level
    survey_inst = get_survey(survey)
    filt_inst = survey_inst.get_filter(filt)
    sky_level = mean_sky_level(survey_inst, filt_inst).value
    assert int(sky_level) == expected
