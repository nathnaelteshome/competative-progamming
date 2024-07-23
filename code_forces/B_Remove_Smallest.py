t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()

    left = 0
    right = 1
    flag = True
    # [1, 1, 2, 4, 5, 5]
    #          l         r
    #
    for right in range(1, len(arr)):
        if arr[right] - arr[left] > 1:
            flag = False
            break
        left += 1
    print("YES" if flag == True else "NO")
