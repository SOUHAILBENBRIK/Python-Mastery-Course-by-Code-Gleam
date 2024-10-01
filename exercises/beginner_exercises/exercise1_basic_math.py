# Problem: Basic Arithmetic Operations
# Question: Write a function that performs basic arithmetic operations (addition, subtraction, multiplication, division) 
# given two numbers and an operator.








def basic_math(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else 'Error: Division by zero'
    else:
        return 'Error: Invalid operator'

# Example usage
print(basic_math(10, 5, '+'))  # Output: 15
