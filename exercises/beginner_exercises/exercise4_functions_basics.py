# Problem: Factorial Calculation
# Question: Implement a function to calculate the factorial of a number using recursion.









def factorial(n):
    if n < 0:
        return 'Error: Negative numbers do not have factorials'
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
