import argparse

from galcheat.helpers import available_surveys, get_survey, print_survey

_FOOTER = "\nprovided by galcheat <https://github.com/aboucaud/galcheat>\n"


def main():
    parser = argparse.ArgumentParser(
        description="Print out the main survey features present in galcheat",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-s", type=str, default=None, metavar="survey_name", help="name of survey"
    )
    args = parser.parse_args()

    if args.survey_name is None:
        for sname in available_surveys:
            survey = get_survey(sname)
            print_survey(survey)
            print("\n", "•  " * 15, "\n")
    else:
        try:
            survey = get_survey(args.survey_name)
            print_survey(survey)
        except ValueError as e:
            print(e)
    print(_FOOTER)


if __name__ == "__main__":
    main()
