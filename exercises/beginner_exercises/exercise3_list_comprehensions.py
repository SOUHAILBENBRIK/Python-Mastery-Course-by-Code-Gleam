# Problem: List Comprehensions
# Question: Use list comprehensions to filter even numbers and square them from a given list.












def filter_and_square_evens(nums):
    return [x**2 for x in nums if x % 2 == 0]

# Example usage
print(filter_and_square_evens([1, 2, 3, 4, 5, 6]))  # Output: [4, 16, 36]
