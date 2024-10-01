# Problem: Context Manager
# Question: Create a custom context manager for handling file operations.








class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Example usage
# with FileHandler('output.txt') as f:
#     f.write('Hello, world!')
