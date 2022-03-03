from galcheat.utilities import mag2counts, mean_sky_level

BTK_COUNTS_MAG24 = {
    "LSST_u": 15321.782101179268,
    "LSST_g": 121397.91888074754,
    "LSST_r": 240956.73939657194,
    "LSST_i": 179448.18815675998,
    "LSST_z": 108953.51289042353,
    "LSST_y": 50727.240442255556,
}

BTK_MEAN_SKY_LEVEL = {
    "LSST_u": 1687.9876819744386,
    "LSST_g": 23241.878848667337,
    "LSST_r": 127057.1381640446,
    "LSST_i": 180301.3875959776,
    "LSST_z": 250784.8105213134,
    "LSST_y": 293292.6831817095,
}


def test_mag2counts():
    survey = "LSST"
    for filt in "ugrizy":
        counts = mag2counts(24, survey, filt).value
        assert counts == int(BTK_COUNTS_MAG24[f"{survey}_{filt}"])


def test_mean_sky_level():
    survey = "LSST"
    for filt in "ugrizy":
        sky_level = mean_sky_level(survey, filt).value
        assert int(sky_level) == int(BTK_MEAN_SKY_LEVEL[f"{survey}_{filt}"])
