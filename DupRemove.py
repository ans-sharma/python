a =[]
final = []
n = int(input("No. of elements"))
for i in range(n):
    a.append(input("Enter the Elements"))

for i in a:
    if i not in final:
        final.append(i)

print(final)
