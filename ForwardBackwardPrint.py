"""Write a program in python that will print a string of text with
step length taken from user and also can print from backwards
with step length taken from user (without slicing technique)."""

strText = input("Enter the Text: ")
iStep = int(input("Enter the Step Length :"))
iMode = int(input("""Enter
1: Forward,
2: Backward
 :"""))
if iMode == 1:
    iStart = 0
    iLen = len(strText)
elif iMode == 2:
    iStart = -1
    iStep = -iStep
    iLen = -len(strText)-1
else:
    print("Wrong Choice")
for letter in range(iStart, iLen, iStep):
    print(strText[letter], end='')

