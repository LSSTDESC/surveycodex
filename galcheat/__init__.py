import pathlib

from galcheat.survey import Survey

SUPPORTED_SURVEYS = ('CFHT', 'DES', 'Euclid', 'HSC', 'HST', 'Rubin')
_datadir = pathlib.Path('galcheat/data')

survey_info = {
    survey: Survey.from_yaml(_datadir / f"{survey}.yaml")
    for survey in SUPPORTED_SURVEYS
}
