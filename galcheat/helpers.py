from pathlib import Path

from galcheat.survey import Survey

_BASEDIR = Path(__file__).parent.resolve()
_survey_info = {
    path.stem: Survey.from_yaml(path) for path in _BASEDIR.glob("data/*.yaml")
}

available_surveys = list(_survey_info.keys())
"List of available surveys in galcheat"


def get_survey(survey_name):
    """Get the dataclass corresponding to the survey

    Parameters
    ----------
    survey_name: str
        Name of a survey among the `available_surveys`

    Returns
    -------
    Survey
        The corresponding Survey dataclass

    Raises
    ------
    ValueError
        When the input survey is not (currently) available

    """
    if survey_name not in available_surveys:
        raise ValueError(
            "Please check the survey name. "
            f"The available surveys are {available_surveys}"
        )

    return _survey_info[survey_name]


def get_filter(filter_name, survey_name):
    """Get the filter class from the corresponding survey

    Parameters
    ----------
    filter_name: str
        Name of a filter belonging to `survey_name`
    survey_name: str
        Name of a survey among the `available_surveys`

    Returns
    -------
    Filter
        The corresponding Filter dataclass

    """
    survey = get_survey(survey_name)

    return survey.get_filter(filter_name)
