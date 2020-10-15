iArr = []
while True:
    iChoice = int(input("""
    Enter 1: Push
          2: Pop
          3: Display
          4: Exit
           : """))
    if iChoice == 1:
        iArr.append(int(input("Enter the No:")))
    elif iChoice == 2:
        if len(iArr) == 0:
            print("Array is Empty!")
        else:
            print("""
        ¯¯|
        %s| is Deleted 
        __|""" %iArr[0])
            iArr.pop(0)
    elif iChoice == 3:
        for i in range(0, len(iArr)):
            if i == len(iArr)-1:
                print("¯¯", end="")
            else:
                print("¯¯|", end="")
        print("")
        for i in range(0, len(iArr)):
            if i == len(iArr)-1:
                print("%s"%iArr[i], end="")
            else:
                print("%s|"%iArr[i], end="")
        print("")
        for i in range(0, len(iArr)):
            if i == len(iArr)-1:
                print("__", end="")
            else:
                print("__|", end="")

    elif iChoice == 4:
        break
    else:
        print("Please Enter a correct choice")

