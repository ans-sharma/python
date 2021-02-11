def countArgs(*kargs):
    noOfArgs = len(kargs)
    if noOfArgs == 1:
        print(noOfArgs)
    elif noOfArgs ==2:
        print(max(kargs))
    elif noOfArgs ==3:
        temp = 0
        for val in kargs:
            temp = temp + val
        print(temp/3)
    else:
        print("More than 3 kargs")


countArgs(5,12)
countArgs(16)
countArgs(1,2,3)
countArgs()
countArgs(1,2,3,1,2,3)