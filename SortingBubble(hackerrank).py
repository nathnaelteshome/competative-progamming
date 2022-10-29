def countSwaps(a):
    i = len(a)
    counter = 0
    while i >= 0:
        for j in range(len(a)):
            if j+1 == len(a):
                break
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                counter += 1
            # print(counter, a)
        i -= 1
    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")


# countSwaps([4, 32, 5, 1, 52])
