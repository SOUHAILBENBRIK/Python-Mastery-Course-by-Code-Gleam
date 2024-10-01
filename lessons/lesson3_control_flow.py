"""
Lesson 3: Control Flow in Python
Objective: Learn how to use if-else statements and loops.
"""

# If-Else Statements
x = 15
if x > 10:
    print("x is greater than 10")  # Output: x is greater than 10
else:
    print("x is 10 or less")

# For Loops
for i in range(1, 6):
    print(i)                       # Output: 1 2 3 4 5

# While Loops
counter = 0
while counter < 3:
    print(counter)                 # Output: 0 1 2
    counter += 1

# Break and Continue
for letter in "python":
    if letter == "h":
        break
    print(letter)                  # Output: p y t

# EXERCISE:
# 1. Write a program that prints all the numbers from 1 to 20, but skips numbers that are divisible by 3.
# 2. Use `continue` to skip the numbers and `else` to print a message when done.
