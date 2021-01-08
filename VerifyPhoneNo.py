# 1. Write a program in Python to verify a phone number in the format
# (+91)1234567890.

def phoneNoCheck(phoneNo):
    flag = True
    mask = '(+91)'
    if phoneNo[0:5] == mask and len(phoneNo)-5 == 10:
        for i in range(6, len(phoneNo)):
            if phoneNo[i].isdigit() == False:
                flag = False
                break
    else:
        flag = False
    if flag == True:
        print("It is a Valid Phone No.")
    else:
        print("It is not a Valid Phone No.")


phoneNo = input("Enter the Phone No. :")
phoneNoCheck(phoneNo)
