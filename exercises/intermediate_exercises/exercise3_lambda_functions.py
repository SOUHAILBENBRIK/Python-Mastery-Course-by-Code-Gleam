# Problem: Lambda Functions
# Question: Use lambda functions to filter out negative numbers and sort a list of tuples.








def process_data(data):
    positive_data = list(filter(lambda x: x[0] > 0, data))
    return sorted(positive_data, key=lambda x: x[1])

# Example usage
print(process_data([(1, 'a'), (-2, 'b'), (3, 'c'), (0, 'd')]))  # Output: [(1, 'a'), (3, 'c')]
