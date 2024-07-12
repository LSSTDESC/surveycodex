import argparse

from surveycodex.helpers import available_surveys, print_survey

_FOOTER = "\nprovided by surveycodex <https://github.com/LSSTDESC/surveycodex>\n"
_LINEBREAK = "\n" + "•  " * 15 + "\n"


def _survey_parser():
    parser = argparse.ArgumentParser(
        description="Print out the main survey features present in surveycodex",
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
    parser.add_argument(
        "--rich",
        action="store_true",
        dest="use_rich",
        help="Use rich console for printing.",
    )
    return parser.parse_args()


def main():
    args = _survey_parser()

    use_rich = False
    if args.use_rich:
        try:
            from rich.console import Console

            console = Console()
            use_rich = True
        except ImportError:
            print(
                "The rich library is not installed by default with surveycodex.",
                "In order to use rich printing, please consider installing it using pip.",
                "`python -m pip install rich`",
                "\nDefaulting to classic display...\n",
            )

    if args.survey_name is None:
        surveys = available_surveys
    else:
        surveys = [args.survey_name]

    if use_rich:
        from surveycodex.rich import display_references, display_survey

        for survey in surveys:
            console.print("")
            console.print(display_survey(survey))
            if args.show_refs:
                console.print(display_references(survey))
        console.print(_FOOTER)
    else:
        for survey in surveys:
            print_survey(survey, show_refs=args.show_refs)
            if survey != surveys[-1]:
                print(_LINEBREAK)
        print(_FOOTER)


if __name__ == "__main__":
    main()
