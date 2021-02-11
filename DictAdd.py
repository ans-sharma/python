# Write a Python program to combine two dictionary adding values for common keys.
# Example:
#     d1 = {'a': 100, 'b': 200, 'c':300}
#     d2 = {'a': 300, 'b': 200, 'd':400}
#     Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

a = dict()
b = dict()

def dictInput(dict1): 
    while(int(input("Enter 1: to Add element\nEnter 0: to Exit\n=>"))):
        key = input("Enter the Key:")
        value = int(input("Enter the Value:"))
        dict1.update({key:value}) #String key and int value

print("Enter the value (Dict1):")
dictInput(a)
print("Enter the value (Dict2):")
dictInput(b)

#Input Display
print("First Dict:", end = "")
print(a)
print("Second Dict:", end = "")
print(b)

#main logic
for value in a:
    if value in b:
        a[value] = a[value] + b[value]

for key in b:
    if key not in a:
        a.update({key:b[key]})

#final output
print("After Addition:", end = "")
print(a)
