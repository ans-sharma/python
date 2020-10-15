def Check(value):
    if value <= 0:
        return False
    else:
        return True
iMat1, iMat2, iMat3= [], [] ,[]
while True:
    iChoice = int(input("""Enter 1: Enter value in Matrix 1
      2: Enter value in Matrix 2
      3: Multiplication
      4: Display Matrix
      5: Exit
=>"""))
    if iChoice == 1:
        row1 = int(input("Input Number of Rows:"))
        col1 = int(input("Input Number of Cols:"))
        if Check(row1) and Check(col1):
            pass
        else:
            print("\nIndexing Can't be -ve")
            row1 = col1 = 0
            print("Please reinitialize the Value\n")
        iMat1 = [[int(input('index['+str(i)+"]["+str(j)+"]:")) for j in range(col1)]for i in range(row1)]
        M1Flag = False
    elif iChoice == 2:
        row2 = int(input("Input Number of Rows:"))
        col2 = int(input("Input Number of Cols:"))
        if Check(row2) and Check(col2):
            pass
        else:
            print("\nIndexing Can't be -ve")
            row1 = col1 = 0
            print("Please reinitialize the Value\n")
        iMat2 = [[int(input('index['+str(i)+"]["+str(j)+"]:")) for j in range(col2)]for i in range(row2)]
        M2Flag = False
    elif iChoice == 3:
        if col1 == row2:
            iMat3 = [[0 for j in range(col2)]for i in range(row1)]
            for i in range(row1):
                for j in range(col2):
                    for k in range(col1):
                        iMat3[i][j] += iMat1[i][k] * iMat2[k][j]
            print("Multiplication Done!!\n")
        else:
            print("Multiplication is not Possible")
            print("Error:-\n Matrix1: "+ str(row1)+ "x" + str(col1)+ "\n" + " Matrix2: "+ str(row2)+ "x" + str(col2)+ "\n")
    elif iChoice == 4:
        dChoice = int(input("""Which Matrix do you want to see,
Enter 1, for Matrix 1
      2, for Matrix 2
      3, for Multiplication Matrix
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
            print("Multiplication Matrix:")
            for i in range(row1):
                for j in range(col2):
                    print(iMat3[i][j], end = " ")
                print()
        else:
            print("Wrong Choice, Maybe the Matrix is not initialize.")
    elif iChoice == 5:
        break
    else:
        print("Wrong Choice")
