M1Flag = True
M2Flag = True
iMat1, iMat2, iMat3, iMat4 = [], [] ,[] , []
while True:
    iChoice = int(input("""Enter 1: Enter value in Matrix 1
      2: Enter value in Matrix 2
      3: Addition
      4: Substraction
      5: Display Matrix
      6: Exit
=>"""))
    if iChoice == 1:
        row1 = int(input("Input Number of Rows:"))
        col1 = int(input("Input Number of Cols:"))
        if M2Flag == False:
            if row1 != row2 or col1 != col2:
                print("Warning !!! Dimension of Matrix 2 is " + str(row2)+ "x" + str(col2))
        iMat1 = [[int(input('index['+str(i)+"]["+str(j)+"]:")) for j in range(col1)]for i in range(row1)]
        M1Flag = False
    elif iChoice == 2:
        row2 = int(input("Input Number of Rows:"))
        col2 = int(input("Input Number of Cols:"))
        if M1Flag == False:
            if row1 != row2 or col1 != col2:
                print("Warning !!! Dimension of Matrix 1 is " + str(row1)+ "x" + str(col1))
        iMat2 = [[int(input('index['+str(i)+"]["+str(j)+"]:")) for j in range(col2)]for i in range(row2)]
        M2Flag = False
    elif iChoice == 3:
        if row1 == row2 and col1 == col2:
            iMat3 = [[iMat1[i][j] + iMat2[i][j] for j in range(col2)]for i in range(row1)]
        else:
            print("Dimensions of Matrices are not same!!!")
            print("Matrix 1: " + str(row1)+ "x" + str(col1))
            print("Matrix 2: " + str(row2)+ "x" + str(col2))
    elif iChoice == 4:
        if row1 == row2 and col1 == col2:
            iMat4 = [[iMat1[i][j] - iMat2[i][j] for j in range(col2)]for i in range(row1)]
        else:
            print("Dimensions of Matrices are not same!!!")
            print("Matrix 1: " + str(row1)+ "x" + str(col1))
            print("Matrix 2: " + str(row2)+ "x" + str(col2))
    elif iChoice == 5:
        dChoice = int(input("""Which Matrix do you want to see,
Enter 1, for Matrix 1
      2, for Matrix 2
      3, for Addition Matrix
      4, for Substraction Matrix
=>"""))
        if dChoice == 1 and len(iMat1) != 0:
            print("Matrix 1:")
            for i in range(row1):
                for j in range(col1):
                    print(iMat1[i][j], end = " ")
                print()
        elif dChoice == 2 and len(iMat2) != 0:
            print("Matrix 2:")
            for i in range(row2):
                for j in range(col2):
                    print(iMat2[i][j], end = " ")
                print()
        elif dChoice == 3 and len(iMat3) != 0:
            print("Addition Matrix:")
            for i in range(row1):
                for j in range(col1):
                    print(iMat3[i][j], end = " ")
                print()
        elif dChoice == 4 and len(iMat4) != 0:
            print("Substraction Matrix:")
            for i in range(row2):
                for j in range(col2):
                    print(iMat4[i][j], end = " ")
                print()
        else:
            print('Wrong Choice, Maybe the Matrix is not initialize.')
            

    elif iChoice == 6:
        break
    else:
        print("Wrong Choice")






        
"""m = int(input("No. of rows:"))
n = int(input("No. of cols:"))

print("Enter values of matrix 1")
mat1 = [[int(input(":")) for i in range(m)]for j in range(n)]
print("Enter values of matrix 2")
mat2 = [[int(input(":")) for i in range(m)]for j in range(n)]

for i in range(m):
    for j in range(n):
        mat1[i][j]= mat1[i][j] + mat2[i][j]

print("Final matrix")
for i in range(m):
    for j in range(n):
        print(mat1[i][j], end=" ")
    print("")
"""
