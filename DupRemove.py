a =[]
final = []
n = int(input("No. of elements: "))
print("Enter the Elements")
for i in range(n):
    a.append(input("=>"))

for i in a:
    if i not in final:
        final.append(i)

print("List After Removing Duplicates: ", end="")
print(final)
