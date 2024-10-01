# Problem: Unit Testing
# Question: Write unit tests for a function that calculates the factorial of a number.








import unittest

def factorial(n):
    if n < 0:
        return 'Error: Negative numbers do not have factorials'
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-1), 'Error: Negative numbers do not have factorials')

# Example usage
# if __name__ == '__main__':
#     unittest.main()
