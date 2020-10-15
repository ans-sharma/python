import random
size = int(input("Enter the size of list: "))
print("Enter the value")
a = []
for i in range(0, size):
    item = input()
    a.append(item)
while True:
    print("Enter 1 to display random value\n    2 for exit")
    choice = int(input(":"))
    if choice == 1:
        print(a[random.randint(0,len(a)-1)])
    elif choice ==2:
        exit()