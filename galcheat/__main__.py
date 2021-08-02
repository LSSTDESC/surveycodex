from galcheat import survey_info


def main():
    for survey, info in survey_info.items():
        print(survey, ":")
        print("  ", info)
        print("   Filters :")
        for filtinfo in info.get_filters():
            print("     ", filtinfo)
        print()


if __name__ == "__main__":
    main()
