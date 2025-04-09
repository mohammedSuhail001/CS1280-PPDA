def merge_dictionaries():
    dict1 = eval(input("Enter the first dictionary: "))
    dict2 = eval(input("Enter the second dictionary: "))

    merged_dict = {**dict1, **dict2}
    print("\nMerged Dictionary:", merged_dict)

merge_dictionaries()
