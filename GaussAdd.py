iRange = int(input("Enter the range:"))
sum = 0
for i in range(1, iRange+1):
    print(str(i) + " + " + str((iRange+1)-i) + " = " + str(i + ((iRange+1)-i)))
    sum = sum + i + (iRange+1)-i
print("sum:" + str(sum/2))