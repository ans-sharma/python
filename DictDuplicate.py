# Write a Python program to remove duplicates from Dictionary.
dict1 = dict()
def dictInput(dict1):
    while(int(input("Enter 1: to Add element\nEnter 0: to Exit\n=>"))):
        key = input("Enter the Key:")
        value = input("Enter the Value:")
        dict1.update({key:value})

print("Enter the value (Dict1):")
# dict1 = {'1': '12', '2': '13', '3': '14', '4': '14','5': '14'}
dictInput(dict1)
print("Dict:", end = "")
print(dict1)

keysToPop = ""
for i in dict1:
    for j in dict1:
        if dict1[i]==dict1[j] and i!=j and i not in keysToPop:
            keysToPop += j
for i in keysToPop:
    dict1.pop(i)

print("Final Dict:", end = "")
print(dict1)
