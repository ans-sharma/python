import random

intUpperRange = int(input("Enter the No of Elements to be Added: "))

while True:
    strTemp = ""
    intSum = 0
    for i in range (0, intUpperRange):
        if i < intUpperRange-1:
            iTemp = random.randint(10,99)
            intSum = intSum + iTemp
            strTemp = strTemp + str(iTemp) + " + "
        else:
            iTemp = random.randint(10,99)
            intSum = intSum + iTemp
            strTemp = strTemp + str(iTemp) + " = "
    print(strTemp)
    input("Press any key to see the answer: ")
    print("Ans = {}".format(intSum))
    print("---------------")