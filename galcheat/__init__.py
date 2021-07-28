import pathlib

from galcheat.survey import Survey

# SURVEYS = ['CFHT', 'DES', 'Euclid', 'HSC', 'HST', 'Rubin']
SUPPORTED_SURVEYS = ['Rubin']
_datadir = pathlib.Path('galcheat/data')

survey_info = {
    survey: Survey.from_yaml(_datadir / f"{survey}.yaml")
    for survey in SUPPORTED_SURVEYS
}
