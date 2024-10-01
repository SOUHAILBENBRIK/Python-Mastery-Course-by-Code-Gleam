"""
Lesson 2: Python Data Structures
Objective: Understand Lists, Tuples, Dictionaries, and Sets.
"""

# Lists: An ordered, mutable collection of elements
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")      # Add an item
print(fruits)                # Output: ['apple', 'banana', 'cherry', 'orange']

# Tuples: An ordered, immutable collection
point = (4, 5)
print(point[0])              # Output: 4

# Dictionaries: Key-Value pairs
student = {"name": "John", "age": 21}
student["grade"] = "A"       # Add new key-value
print(student)               # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

# Sets: Unordered collection of unique elements
numbers = {1, 2, 3, 3, 4}
print(numbers)               # Output: {1, 2, 3, 4}

# EXERCISE:
# 1. Create a dictionary representing a book with keys: title, author, and year.
# 2. Add a new key 'genre' and print the updated dictionary.
