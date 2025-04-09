# Extend the dictionary merge program to handle cases where the two dictionaries have overlapping keys. If a key exists in both dictionaries, the merged dictionary should add the values of the overlapping keys.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  
        else:
            merged_dict[key] = value
    return merged_dict

# Example usage
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 40}
merged = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged)
