"""Write a program in python that will check whether
a string is a palindrome or not."""
strTemp = ""
strText = input("Enter a String: ")
strText = strText.lower()
for letter in range(-1, -len(strText)-1, -1):
    strTemp = strTemp + strText[letter]
if strTemp == strText:
    print(strText.title() + ", is  a Palindrome")
else:
    print("Its not a Palindrome")
