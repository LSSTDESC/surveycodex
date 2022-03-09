from galcheat.helpers import available_surveys, get_survey


def main():
    for survey_name in available_surveys:
        survey = get_survey(survey_name)
        print(survey_name, ":")
        print("  ", survey)

        print("   Filters :")
        for info in survey.filters.values():
            print("     ", info)
        print()


if __name__ == "__main__":
    main()
