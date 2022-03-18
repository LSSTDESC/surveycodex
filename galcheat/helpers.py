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
    survey_name : str
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


def print_survey(survey, show_refs=False):
    """Print information on a given survey

    Parameters
    ----------
    survey : str or Survey
        The survey name or Survey instance
    show_refs : bool
        Print the references for each parameter.

    """
    if not isinstance(survey, Survey):
        survey = get_survey(survey)

    print(survey)
    for filter_name in survey.available_filters:
        print(survey.get_filter(filter_name))
    if show_refs:
        print_references(survey.references)


def print_references(references):
    """Pretty print the references of the survey and filter parameters

    The references are composed of a link and a sentence for comments.

    Parameters
    ----------
    references : dict
        Dictionary with the references for each parameter

    """
    name_size = max(len(name) for name in references)
    link_size = max(len(param["link"]) for param in references.values())
    comment_size = max(len(param["comment"]) for param in references.values())
    header = f"{'Parameter name':<{name_size}} | {'Reference link':<{link_size}} | {'Comments':<{comment_size}}"

    print("\n-=[ References ]=-\n")
    print(header)
    print("-" * len(header))
    for name, param in references.items():
        print(
            f"{name:<{name_size}} | {param['link']:<{link_size}} | {param['comment']:<{comment_size}}"
        )
    print("-" * len(header))
