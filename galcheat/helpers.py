from pathlib import Path

from galcheat.filter import Filter
from galcheat.survey import Survey

_BASEDIR = Path(__file__).parent.resolve()
_survey_info = {
    path.stem: Survey.from_yaml(path) for path in _BASEDIR.glob("data/*.yaml")
}

available_surveys = list(_survey_info.keys())


def get_survey(survey_name: str) -> Survey:
    """Get the dataclass corresponding to the survey

    Parameters
    ----------
    survey_name: str
        Name of a survey among the `available_surveys`

    Returns
    -------
    a Survey dataclass

    Raises
    ------
    ValueError: when the input survey is not (currently) available

    """
    if survey_name not in available_surveys:
        raise ValueError(
            "Please check the survey name. "
            f"The available surveys are {available_surveys}"
        )

    return _survey_info[survey_name]


def get_filter(filter_name: str, survey_name: str) -> Filter:
    """Get the filter class from the corresponding survey

    Parameters
    ----------
    filter_name: str
        Name of a filter belonging to `survey_name`
    survey_name: str
        Name of a survey among the `available_surveys`

    Returns
    -------
    a Filter dataclass

    Raises
    ------
    ValueError: when the survey or filter is not available

    """
    survey = get_survey(survey_name)

    return survey.get_filter(filter_name)
