"""Write a Python function that takes a list of
words and returns the length of the longest one."""
print("Enter list of word, with comma(,) as a separator between them.")
words = input("Enter the String: ")
words = words.split(',')
length = 0
for word in words:
    if len(word.strip()) > length:
        length = len(word.strip())
print("Length of the Longest Word is "+ str(length) + ".")
