# Problem: Generators
# Question: Create a generator that yields the square of numbers up to n.








def square_generator(n):
    for i in range(n):
        yield i ** 2

# Example usage
for square in square_generator(5):
    print(square)  # Output: 0, 1, 4, 9, 16
