value = input("Enter the value: ")
flag = False
for i in range(0, len(value)):
    if value[i] == "-":
        if i == len(value)-1:
            flag = True
            print("Not a Number")
            break
        elif ord(value[i+1]) < 48 or ord(value[i+1]) > 57:
            flag = True
            print("Not a Number")
            break
    elif ord(value[i]) < 48 or ord(value[i]) > 57:
        print("Not a Number")
        flag = True
        break
if flag == False:
    print("Its a Number")
