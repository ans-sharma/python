"""Write a program in python that will take a string
and number K from user and extract first K consecutive
digits making number."""

strText = input("Enter the String: ")
iK = int(input("Enter the Value of K: "))
iNum = list(range(0, 10))
iCount = 0
for letter in range(0, len(strText)):
    if strText[letter] in str(iNum) and strText[letter] != ' ':
        print(strText[letter], end='')
        iCount = iCount + 1
    if iCount==iK:
        break;
