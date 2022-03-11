import argparse

from galcheat.helpers import available_surveys, print_survey

_FOOTER = "\nprovided by galcheat <https://github.com/aboucaud/galcheat>\n"
_LINEBREAK = "\n" + "•  " * 15 + "\n"


def _survey_parser():
    parser = argparse.ArgumentParser(
        description="Print out the main survey features present in galcheat",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-s",
        type=str,
        default=None,
        dest="survey_name",
        help="Name of survey. If None, shows all available surveys.",
    )
    parser.add_argument(
        "--refs",
        action="store_true",
        dest="show_refs",
        help="Print the references for each parameter.",
    )
    return parser.parse_args()


def main():
    args = _survey_parser()

    if args.survey_name is None:
        for survey in available_surveys:
            print_survey(survey, show_refs=args.show_refs)
            print(_LINEBREAK)
    else:
        try:
            print_survey(args.survey_name, show_refs=args.show_refs)
        except ValueError as e:
            print(e)
    print(_FOOTER)


if __name__ == "__main__":
    main()
