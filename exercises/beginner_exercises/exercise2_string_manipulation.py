# Problem: String Manipulation
# Question: Create a function to reverse a string, remove vowels, and convert to uppercase.











def manipulate_string(s):
    reversed_str = s[::-1]
    no_vowels = ''.join([char for char in reversed_str if char.lower() not in 'aeiou'])
    return no_vowels.upper()

# Example usage
print(manipulate_string("Hello World"))  # Output: "DLRW LLH"
