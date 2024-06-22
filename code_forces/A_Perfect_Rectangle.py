t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    summation = sum(arr)  # 16, 28
    right = max(arr) + 1
    left = -1

    num = int(summation**0.5)
    if num**2 == summation:
        print("YES")
    else:
        print("NO")
