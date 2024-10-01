# Problem: Fibonacci Sequence
# Question: Generate a Fibonacci sequence up to a given number n.










def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:-1]  # Exclude the last element if it exceeds n

# Example usage
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8]
