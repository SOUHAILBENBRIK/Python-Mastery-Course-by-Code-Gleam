"""
Lesson 5: File Handling in Python
Objective: Learn how to read from and write to files.
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)           # Output: Hello, World!\nThis is a file handling example.

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Output: Hello, World! \n This is a file handling example.

# EXERCISE:
# 1. Write a program to append a new line to "example.txt" and print the updated file content.
# 2. Create a function that reads a file and returns the number of lines it contains.
