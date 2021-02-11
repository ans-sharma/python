# Write a Python script to concatenate following dictionaries to create a new one.
dict1 = dict()
dict2 = dict()
dict3 = dict()

def dictInput(dict1):
    while(int(input("Enter 1: to Add element\nEnter 0: to Exit\n=>"))):
        key = input("Enter the Key:")
        value = input("Enter the Value:")
        dict1.update({key:value})

print("Enter the value (Dict1):")
dictInput(dict1)
print("Enter the value (Dict2):")
dictInput(dict2)

dict3.update(dict1)
dict3.update(dict2)

print("First Dict:", end = "")
print(dict1)
print("Second Dict:", end = "")
print(dict2)
print("Concatenated Dict:", end = "")
print(dict3)

