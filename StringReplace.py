a = input("Enter the String: ")
re = input("Enter the word which you want to replace: ")
re1 = input("New Word: ")
print("Original String: ", end="")
print(a)
a = a.split()
for i in range(len(a)):
    if a[i] == re:
        a[i]= re1
b = ""
for i in a:
    b= b + " " + i 
print("Modefied String:", end="")
print(b)
