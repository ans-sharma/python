l = [[1,2],["a","b","c"], 15, (5,2), 45, 32]
count = 0
for i in l:
    if type(i) == tuple:
        break
    else:
        count=count+1
print("No. of elements = " + str(count))
