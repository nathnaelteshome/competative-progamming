t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    min_val = 10**10

    for idx in range(1, len(arr)):
        min_val = min(min_val, max(arr[idx - 1], arr[idx]))

    print(min_val - 1)
