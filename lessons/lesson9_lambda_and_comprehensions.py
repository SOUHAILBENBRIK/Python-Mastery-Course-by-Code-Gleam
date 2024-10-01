"""
Lesson 9: Lambda Functions and List Comprehensions
Objective: Understand how to use lambda functions and list comprehensions for concise code.
"""

# Lambda functions
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Using lambda with filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# List comprehensions
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# EXERCISE:
# 1. Write a lambda function to find the maximum of three numbers.
# 2. Use list comprehension to create a list of the lengths of each word in a given sentence.
