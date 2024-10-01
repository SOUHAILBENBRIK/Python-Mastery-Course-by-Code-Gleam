"""
Lesson 10: Decorators and Context Managers
Objective: Learn how to use decorators to modify functions and context managers for resource management.
"""

# A simple decorator
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed."

print(display())  # Output: Wrapper executed before display

# Using a context manager
class SampleContext:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")

with SampleContext() as sample:
    print("Inside the context.")  # Output: Inside the context.

# EXERCISE:
# 1. Create a decorator that logs the execution time of a function.
# 2. Write a context manager that opens a file and automatically closes it after reading.
