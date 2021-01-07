rows = int(input("Enter the no. of rows: "))
print("Pascal's Triangle")
for i in range(0, rows):
    for space in range(1, (rows+1)-i):
        print(" ", end="")
    for j in range(0, i+1):
        if j == 0 or i == 0:
            one = 1
        else:
            one = int(one * (i-j+1)/j)
        print(" " + str(one), end="")
    print("")
