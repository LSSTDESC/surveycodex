from galcheat import survey_info

for survey, info in survey_info.items():
    print(survey, ":")
    print("  ", info)
    print("   Filters :")
    for filtinfo in info.get_filters():
        print("     ", filtinfo)
    print()
