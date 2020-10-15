tuples = [(1, 2, 3), ('x', 'a', 'b'), (''), ('1', '2'), (), ('', ''), ()]
print("Original List: ", end="")
print(tuples)
new = []
for i in tuples:
    if i:
        new.append(i)
print("After tuple removal: ", end="")
print(new)