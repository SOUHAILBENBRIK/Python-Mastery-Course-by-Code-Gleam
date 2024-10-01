"""
Lesson 8: Generators and Iterators
Objective: Learn how to create and use generators for efficient iteration.
"""

# Defining a generator
def count_up_to(max):
    """Generator that counts up to a maximum number."""
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5

# Generator expression
squared_numbers = (x**2 for x in range(5))
for square in squared_numbers:
    print(square)  # Output: 0 1 4 9 16

# EXERCISE:
# 1. Create a generator that yields even numbers up to a given limit.
# 2. Write an iterator class that iterates over a collection of names and returns them in uppercase.
