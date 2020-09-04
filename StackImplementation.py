iArr = []
while True:
    iChoice = int(input("""
    Enter 1: Push
          2: Pop
          3: Peek
          4: Display
          5: Exit
           : """))
    if iChoice == 1:
        iArr.append(int(input("Enter the No:")))
    elif iChoice == 2:
        if len(iArr) == 0:
            print("Array is Empty!")
        else:
            print("""      |_""" + str(iArr[len(iArr)-1]) + """_|  is Poped""")
            iArr.pop()
    elif iChoice == 3:
        if len(iArr) == 0:
            print("Array is Empty!")
        else:
            print("""      |_""" + str(iArr[len(iArr)-1]) + """_|""")
    elif iChoice == 4:
        for i in range(-1, -(len(iArr)+1), -1):
            print("""      |_""" + str(iArr[i]) + """_|""")
    elif iChoice == 5:
        break
