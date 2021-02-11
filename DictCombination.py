# Write a Python program to create and display all combinations of letters, selecting each letter
# from a different key in a dictionary.

dict1 = {'1': 'ab', '2': 'cd', '3': 'efg', '4': 'hi'}
String = ""
for i in dict1:
    String = String + dict1[i]
s = list(String)
# print(s)
for i in range(0, len(s)):
    for j in range(0, len(s)-1):
        temp = s[j]
        s[j]=s[j+1]
        s[j+1]=temp
        print(s)
        