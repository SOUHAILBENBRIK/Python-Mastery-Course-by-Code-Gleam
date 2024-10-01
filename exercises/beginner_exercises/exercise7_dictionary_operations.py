# Problem: Dictionary Operations
# Question: Create a function to merge two dictionaries and update values if keys match.











def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  # Copy first dictionary
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Update value if key exists
        else:
            merged[key] = value  # Add new key-value pair
    return merged

# Example usage
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # Output: {'a': 1, 'b': 5, 'c': 4}
