from galcheat.helpers import available_surveys, get_survey


def main():
    for survey_name in available_surveys:
        survey = get_survey(survey_name)
        print(survey_name, ":")
        print("  ", survey)

        survey_filters = survey.get_filters()
        print("   Filters :")
        for info in survey_filters.values():
            print("     ", info)
        print()


if __name__ == "__main__":
    main()
