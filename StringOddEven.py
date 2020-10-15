sString = input("Enter the String: ")
sList = sString.split()
sEven, sOdd = "",""
for i in range(len(sList)):
    if i%2 == 0:
        sEven = sEven + " " + sList[i]
    else:
        sOdd = sOdd + " " + sList[i]
print("Even Strings:" + str(sEven) )
print("Odd Strings:" + str(sOdd))
