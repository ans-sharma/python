iLow = int(input("Enter lower limit: "))
iHigh = int(input("Enter upper limit: "))
print("Armstrong Numbers are: ")
for iNum in range(iLow, iHigh+1):
    iLen = len(str(iNum))
    iTemp = iNum
    iSum = 0
    while(iNum > 0):
        iDigit = iNum%10
        iSum = iSum + (iDigit**iLen)
        iNum = iNum//10
    if iSum == iTemp:
        print(iSum, end=',')

#New