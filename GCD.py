iNum = int(input("Enter a Number: "))
iNum2 = int(input("Enter a Number: "))
if iNum < iNum2:
    iTemp = iNum
    iNum = iNum2
    iNum2 = iTemp
while iNum2>0:
    iTemp = iNum%iNum2
    iNum = iNum2
    iNum2 = iTemp
print("GCD is ", iNum)