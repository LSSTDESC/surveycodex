from galcheat.utilities import mag2counts, mean_sky_level

BTK_COUNTS_MAG24 = {
    "Rubin_u": 15321.782101179268,
    "Rubin_g": 121397.91888074754,
    "Rubin_r": 240956.73939657194,
    "Rubin_i": 179448.18815675998,
    "Rubin_z": 108953.51289042353,
    "Rubin_y": 50727.240442255556,
}

BTK_MEAN_SKY_LEVEL = {
    "Rubin_u": 1687.9876819744386,
    "Rubin_g": 23241.878848667337,
    "Rubin_r": 127057.1381640446,
    "Rubin_i": 180301.3875959776,
    "Rubin_z": 250784.8105213134,
    "Rubin_y": 293292.6831817095,
}


def test_mag2counts():
    survey = "Rubin"
    for filt in "ugrizy":
        counts = mag2counts(24, survey, filt).value
        assert counts == int(BTK_COUNTS_MAG24[f"{survey}_{filt}"])


def test_mean_sky_level():
    survey = "Rubin"
    for filt in "ugrizy":
        sky_level = mean_sky_level(survey, filt).value
        assert int(sky_level) == int(BTK_MEAN_SKY_LEVEL[f"{survey}_{filt}"])
