n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

if arr[:n] == arr[n:]:
    print(-1)
else:
    print(*arr)