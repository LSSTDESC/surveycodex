from galcheat.helpers import get_survey


def test_survey_copy_not_view():
    survey = get_survey("LSST")
    original_obscuration = survey.obscuration
    new_obscuration = 42
    survey.obscuration = new_obscuration
    assert survey.obscuration == new_obscuration
    survey2 = get_survey("LSST")
    assert survey2.obscuration == original_obscuration


def test_surveyfilter_copy_not_view():
    survey = get_survey("LSST")
    filter_u = survey.get_filter("u")
    original_zeropoint = filter_u.zeropoint
    new_zeropoint = 42.0 * original_zeropoint.unit
    filter_u.zeropoint = new_zeropoint
    assert filter_u.zeropoint == new_zeropoint
    filter_u2 = get_survey("LSST").get_filter("u")
    assert filter_u2.zeropoint == original_zeropoint


def test_filter_copy_not_view():
    survey = get_survey("LSST")
    filter_u = survey.get_filter("u")
    original_zeropoint = filter_u.zeropoint
    new_zeropoint = 42.0 * original_zeropoint.unit
    filter_u.zeropoint = new_zeropoint
    assert filter_u.zeropoint == new_zeropoint
    filter_u2 = survey.get_filter("u")
    assert filter_u2.zeropoint == original_zeropoint
