"""Write a Python program to get a string from a given string
where all occurrences of its first char have been changed to
'$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t """

strText = input("Enter the String: ");
strFinal = strText[0]
for letter in range(1, len(strText)):
    if strText[letter] == strText[0].lower() or strText[letter] == strText[0].upper():
        strFinal = strFinal + "$"
    else:
        strFinal = strFinal + strText[letter]
print(strFinal)
