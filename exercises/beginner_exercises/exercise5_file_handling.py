# Problem: File Handling
# Question: Write a script to read a text file, count the number of words, 
# and display the frequency of each word.








def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    word_freq = {word: words.count(word) for word in set(words)}
    return word_freq

# Example usage
# Make sure to create a text file named 'sample.txt' before running this
# print(word_count('sample.txt'))
