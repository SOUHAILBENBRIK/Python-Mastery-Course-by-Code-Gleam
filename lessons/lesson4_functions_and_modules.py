"""
Lesson 4: Functions and Modules
Objective: Understand how to define functions, use parameters, return values, and import modules.
"""

# Defining a function
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!

# Function with default parameters
def multiply(a, b=1):
    """Multiply two numbers, b defaults to 1."""
    return a * b

print(multiply(5))       # Output: 5
print(multiply(5, 3))    # Output: 15

# Return multiple values
def get_stats(numbers):
    """Return min, max, and sum of a list."""
    return min(numbers), max(numbers), sum(numbers)

stats = get_stats([1, 2, 3, 4, 5])
print(stats)             # Output: (1, 5, 15)

# Importing modules
import math

# Using a function from the math module
print(math.sqrt(16))     # Output: 4.0

# EXERCISE:
# 1. Write a function that takes a list of numbers and returns the average.
# 2. Import the random module and generate a random number between 1 and 10.
