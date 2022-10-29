

def insertionSort1(n, arr):
    last = arr[-1]
    i = n-1
    temp = arr[i]
    while i > 0 and arr[i-1] > temp:
        arr[i] = arr[i-1]
        print(" ".join(str(e) for e in arr))
        i -= 1
    arr[i] = last
    print(" ".join(str(e) for e in arr))


# insertionSort1(5, [ 2, 4, 6, 8, 3])
