# Problem: Anagram Checker
# Question: Create a function to check if two given strings are anagrams.









def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("listen", "silent"))  # Output: True
