import copy
t = int(input())
while(t!=0):
    t = t-1  
    n = int(input())
    a = input().split(" ")
    z = 1
    vals = [0 for i in range(0, n)]
    temp2 = copy.deepcopy(a)
    temp2.sort(reverse=True)
    for tempVal in temp2:
        for i in range(0,len(a)):
            if int(tempVal) == int(a[i]):
                vals[i] = z
                z = z +1
                a[i] = 99999
                break
    for v in vals:
        print(v, end=" ")   
