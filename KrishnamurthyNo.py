import math
iLow = int(input("Enter lower limit: "))
iHigh = int(input("Enter upper limit: "))
print("Krishnamurthy Numbers are: ")
for iNum in range(iLow, iHigh+1):
    iTemp = iNum
    iSum = 0
    while(iNum > 0):
        iDigit = iNum%10
        iSum = iSum + math.factorial(iDigit)
        iNum = iNum//10
    if iSum == iTemp:
        print(iTemp, end=',')
    
    