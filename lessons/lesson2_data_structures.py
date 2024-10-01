"""
Lesson 2: Python Data Structures
Objective: Understand Lists, Tuples, Dictionaries, and Sets.
"""

# Lists: An ordered, mutable collection of elements
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")      # Add an item
print(fruits)                # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.remove("banana")      # Remove an item
print(fruits)                # Output: ['apple', 'cherry', 'orange']

fruits[0] = "kiwi"           # Edit an item
print(fruits)                # Output: ['kiwi', 'cherry', 'orange']

# Tuples: An ordered, immutable collection
point = (4, 5)
print(point[0])              # Output: 4

# Note: You cannot change a tuple's value directly
# To "edit" a tuple, you need to convert it to a list
point_list = list(point)     # Convert to a list
point_list[0] = 10           # Change value
point = tuple(point_list)    # Convert back to a tuple
print(point)                 # Output: (10, 5)

# Dictionaries: Key-Value pairs
student = {"name": "John", "age": 21}
student["grade"] = "A"       # Add new key-value
print(student)               # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

student["age"] = 22          # Edit existing value
print(student)               # Output: {'name': 'John', 'age': 22, 'grade': 'A'}

del student["grade"]         # Delete a key-value pair
print(student)               # Output: {'name': 'John', 'age': 22}

# Sets: Unordered collection of unique elements
numbers = {1, 2, 3, 3, 4}
print(numbers)               # Output: {1, 2, 3, 4}

numbers.add(5)               # Add an item
print(numbers)               # Output: {1, 2, 3, 4, 5}

numbers.discard(2)           # Remove an item (no error if not found)
print(numbers)               # Output: {1, 3, 4, 5}

# EXERCISE:
# 1. Create a dictionary representing a book with keys: title, author, and year.
book = {"title": "1984", "author": "George Orwell", "year": 1949}
print(book)                 # Output: {'title': '1984', 'author': 'George Orwell', 'year': 1949}

# 2. Add a new key 'genre' and print the updated dictionary.
book["genre"] = "Dystopian"
print(book)                 # Output: {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'genre': 'Dystopian'}

# 3. Update the 'year' of publication to 1950 and print the updated dictionary.
book["year"] = 1950
print(book)                 # Output: {'title': '1984', 'author': 'George Orwell', 'year': 1950, 'genre': 'Dystopian'}

# 4. Delete the key 'author' and print the updated dictionary.
del book["author"]
print(book)                 # Output: {'title': '1984', 'year': 1950, 'genre': 'Dystopian'}
