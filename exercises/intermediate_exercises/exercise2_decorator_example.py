# Problem: Decorator Example
# Question: Implement a simple decorator to log the execution time of a function.
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def example_function():
    time.sleep(1)

# Example usage
# example_function()  # Output: Execution time: 1.0000 seconds
