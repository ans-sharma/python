upperBound = int(input("Enter the Upper Limit: "))
for a in range(1, upperBound+1):
    for b in range(a, upperBound+1):
        pow_cal = pow(a, 2) + pow(b, 2)
        num = pow(pow_cal, 0.5)
        if num % 1 == 0:
            print("(" + str(a) + "," + str(b) + "," + str(int(num)) + ")")
