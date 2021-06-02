t = int(input())
while(t!=0):
    t = t -1
    nk = input().split(" ")
    a = input().split(" ")
    n = int(nk[0])
    while(n!=0):
        val = 0
        n = n-1
        b = input()
        for i in range(0,len(b)):
            if int(b[i]) == 1:
                val = val + int(a[i])
        print(val)
    n = int(nk[0])