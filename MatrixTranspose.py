iRow = int(input("Enter the no. of rows: "))
iCol = int(input("Enter the no. of cols: "))
if iRow <=0 or iCol <= 0:
    print("Matrix indexing can not be -ve or 0.")
    exit()
iMat = [[int(input('index['+str(i)+"]["+str(j)+"]:")) for j in range(iCol)]for i in range(iRow)]
iMat1 = [[0 for j in range(iRow)]for i in range(iCol)]
print("Original Matrix:")
for i in range(iRow):
    for j in range(iCol):
        iMat1[j][i] = iMat[i][j]
        print(iMat[i][j], end=" ")
    print()
print("Transpose Matrix:")
for i in range(iCol):
    for j in range(iRow):
        print(iMat1[i][j], end=" ")
    print()
