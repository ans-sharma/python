l = []
size = int(input("Enter the size of list: "))
for i in range(0,size):
    sChoice = input("""Enter:
        (N)ormal Element
        (L)ist
        (T)uple\n=>""")
    if sChoice == "N" or sChoice == "n":
        iVlaue = input("Enter the Value:")
        l.append(iVlaue)
        print("Element Inserted Successfully\n")
    elif sChoice == "L" or sChoice == "l":
        lSize = int(input("Enter the size of List: "))
        print("Input the Values: ")
        iVlaue = [input("=>") for i in range(0, lSize)]
        l.append(iVlaue)
        print("List Inserted Successfully\n")
    elif sChoice == "T" or sChoice == "t":
        tSize = int(input("Enter the size of Tuple: "))
        print("Input the Values: ")
        iVlaue = tuple(input("=>") for i in range(0, tSize))
        l.append(iVlaue)
        print("Tuple Inserted Successfully\n")
    else:
        print("Wrong Input!")
print("\nThe List is: ", end = "")
print(l)
count = 0
for i in l:
    if type(i) == tuple:
        break
    else:
        count=count+1
print("No. of elements = " + str(count))
