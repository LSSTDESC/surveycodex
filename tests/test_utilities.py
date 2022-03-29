import numpy as np
import pytest

from galcheat.helpers import get_survey
from galcheat.utilities import mag2counts, mean_sky_level

WLD_COUNTS_MAG24 = {
    "LSST_u": 15388.800000000001,
    "LSST_g": 121680.0,
    "LSST_r": 241224.00000000003,
    "LSST_i": 178627.19999999998,
    "LSST_z": 108864.0,
    "LSST_y": 50784.0,
}

WLD_SKY_LEVEL = {
    "LSST_u": 1695.370986797218,
    "LSST_g": 23295.88385352744,
    "LSST_r": 127198.06540061244,
    "LSST_i": 179476.4959914193,
    "LSST_z": 250578.77335308882,
    "LSST_y": 293620.8532702446,
}


@pytest.fixture(
    params=[("LSST", f) for f in "ugrizy"], ids=lambda x: f"survey:{x[0]}-filter:{x[1]}"
)
def lsst_btk_counts(request):
    survey, filt = request.param
    expected = int(WLD_COUNTS_MAG24[f"{survey}_{filt}"])
    return survey, filt, expected


@pytest.fixture(
    params=[("LSST", f) for f in "ugrizy"], ids=lambda x: f"survey:{x[0]}-filter:{x[1]}"
)
def lsst_btk_sky_level(request):
    survey, filt = request.param
    expected = WLD_SKY_LEVEL[f"{survey}_{filt}"]
    return survey, filt, expected


def test_mag2counts_str(lsst_btk_counts):
    survey, filt, expected = lsst_btk_counts
    np.testing.assert_allclose(mag2counts(24, survey, filt).value, expected, rtol=1e-1)


def test_mag2counts_filter_str(lsst_btk_counts):
    survey, filt, expected = lsst_btk_counts
    survey_inst = get_survey(survey)
    np.testing.assert_allclose(
        mag2counts(24, survey_inst, filt).value, expected, rtol=1e-1
    )


def test_mag2counts_filter_instance(lsst_btk_counts):
    survey, filt, expected = lsst_btk_counts
    survey_inst = get_survey(survey)
    filt_inst = survey_inst.get_filter(filt)
    np.testing.assert_allclose(
        mag2counts(24, survey, filt_inst).value, expected, rtol=1e-1
    )


def test_mean_sky_level_str(lsst_btk_sky_level):
    survey, filt, expected = lsst_btk_sky_level
    sky_level = mean_sky_level(survey, filt).value
    np.testing.assert_allclose(sky_level, expected, rtol=1e-1)


def test_mean_sky_level_filter_str(lsst_btk_sky_level):
    survey, filt, expected = lsst_btk_sky_level
    survey_inst = get_survey(survey)
    sky_level = mean_sky_level(survey_inst, filt).value
    np.testing.assert_allclose(sky_level, expected, rtol=1e-1)


def test_mean_sky_level_filter_instance(lsst_btk_sky_level):
    survey, filt, expected = lsst_btk_sky_level
    survey_inst = get_survey(survey)
    filt_inst = survey_inst.get_filter(filt)
    sky_level = mean_sky_level(survey_inst, filt_inst).value
    np.testing.assert_allclose(sky_level, expected, rtol=1e-1)
