"""
Lesson 6: Error Handling in Python
Objective: Learn about exceptions and how to handle errors gracefully.
"""

# Handling exceptions with try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")  # Output: Error: Division by zero is not allowed!

# Catching multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")  # Output: Error: invalid literal for int() with base 10: 'abc'

# Finally block
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution complete.")  # Output: Execution complete.

# EXERCISE:
# 1. Write a program that prompts the user for a number and handles the potential ValueError if the input is not a number.
# 2. Create a function that attempts to open a file and returns a custom error message if it fails.
