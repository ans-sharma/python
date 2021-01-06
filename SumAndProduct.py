def sumAndProduct(end, start = 1):
    pairs = []
    for i in range(start, end):
        for j in range(start, end):
            if i + j == i * j:
                pairs.append("(" + str(i) + "," + str(j) + ")")
    return pairs

if __name__ == "__main__":
    print(sumAndProduct(1000000, start=10000))
