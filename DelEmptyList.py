tuples = [(), ('x','a','b'), ("",), ('1', '2'),('3', 'abc', 'xyz'), ('',''),()]
new = []
for i in tuples:
    if i:
        new.append(i)
print(new)
