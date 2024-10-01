# Problem: Simple Calculator
# Question: Build a simple calculator app that takes user input for operations.









def simple_calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero'
    else:
        return 'Error: Invalid operator'

# Uncomment to run
# print(simple_calculator())
