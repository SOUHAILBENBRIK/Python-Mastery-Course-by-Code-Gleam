"""
Lesson 7: Object-Oriented Programming (OOP)
Objective: Understand classes, objects, inheritance, and encapsulation.
"""

# Defining a class
class Dog:
    """A simple Dog class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Creating an object
my_dog = Dog("Buddy", 3)
print(my_dog.name)          # Output: Buddy
print(my_dog.bark())        # Output: Woof!

# Inheritance
class Puppy(Dog):
    """A Puppy class that inherits from Dog."""
    
    def wag_tail(self):
        return "Wagging tail!"

my_puppy = Puppy("Charlie", 1)
print(my_puppy.wag_tail())  # Output: Wagging tail!

# EXERCISE:
# 1. Create a class `Car` with attributes: make, model, and year. Add a method to display car details.
# 2. Create a subclass `ElectricCar` that adds an attribute for battery size.
