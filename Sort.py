def Merge(a, lowerBound, mid, upperBound):
    k = lowerBound
    i = lowerBound
    j = mid+1
    m = upperBound
    b = []
    b = [0]*len(a)
    while i <= mid and j <= upperBound:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= upperBound:
        b[k] = a[j]
        j += 1
        k += 1
    for z in range(lowerBound, upperBound+1):
        a[z] = b[z]


def mergeSort(a, lowerBound, upperBound):
    if lowerBound < upperBound:
        mid = (upperBound+lowerBound)//2
        mergeSort(a, lowerBound, mid)
        mergeSort(a, mid+1, upperBound)
        Merge(a, lowerBound, mid, upperBound)


def quickSort(a, lowerBound, upperBound):
    if upperBound > lowerBound:
        pivot = lowerBound
        i = lowerBound
        j = upperBound

        while i < j:
            while a[i] <= a[pivot] and i < upperBound:
                i += 1
            while a[j] > a[pivot]:
                j -= 1
            if i < j:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        temp = a[pivot]
        a[pivot] = a[j]
        a[j] = temp

        quickSort(a, lowerBound, j-1)
        quickSort(a, j+1, upperBound)


a = []
while True:
    choice = int(input('''Enter 1: for Input
      2: for QuickSort
      3: for MergeSort
      4: for Display
      5: Exit
=>'''))
    if choice == 1:
        size = int(input("Enter size of Array:  "))
        if size <= 0:
            print("Invalid Array size!\nTry Again")
            continue
        print("Enter the Values")
        for i in range(size):
            Input = int(input())
            a.append(Input)
    elif choice == 2:
        if not a:
            print("Array is Empty")
        else:
            quickSort(a, 0, size-1)
            print("Sorting done! (QuickSort)")
    elif choice == 3:
        if not a:
            print("Array is Empty")
        else:
            mergeSort(a, 0, size-1)
            print("Sorting done! (MergeSort)")
    elif choice == 4:
        if not a:
            print("Array is Empty")
        else:
            print(a)
    elif choice == 5:
        exit()
    else:
        print("Wrong Choice")
