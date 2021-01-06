# Write a program in Python to verify whether the entered input is a number or not.
value = input("Enter the value: ")
flag = False
for i in range(0, len(value)):
    # print(ord(char))
    if value[i] == "-":
        if i == len(value)-1:
            print("Not a number")
            break
        elif ord(value[i+1]) < 48 or ord(value[i+1]) > 57:
            print("Not a number")
            break
    # if flag == True:
    #     if i == len(value)-1:
    #         print("Not a number")
    #         break
    #     elif ord(value[i+1]) < 48 or ord(value[i+1]) > 57:
    #         print("Not a number")
    #         break
    if ord(value[i]) < 48 or ord(value[i]) > 57:
        print("Not a number")
        flag == True
        break
if flag == True:
    print("Its a Number")
# if(flag == False):
#     print("not number")
