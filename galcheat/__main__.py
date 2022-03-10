from galcheat.helpers import available_surveys, get_survey, print_survey

_FOOTER = "\nprovided by galcheat <https://github.com/aboucaud/galcheat>\n"


def main(survey_name=None):
    if survey_name is not None:
        try:
            survey = get_survey(survey_name)
            print_survey(survey)
        except ValueError as e:
            print(e)
            pass
    else:
        for survey_name in available_surveys:
            survey = get_survey(survey_name)
            print_survey(survey)
            print("\n", "•  " * 15, "\n")
    print(_FOOTER)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        main(survey_name=sys.argv[1])
    else:
        main()
