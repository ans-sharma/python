n = int(input())

def BMI(M, H):
    return M / (H*H)

while(n!=0):
    val = input().split(" ")
    temp = BMI(int(val[0]), int(val[1]))
    if temp <= 18:
        print(1)
    elif temp >= 19 and temp <= 24:
        print(2)
    elif temp >= 25  and temp <= 29:
        print(3)
    else:
        print(4)
    n = n -1

