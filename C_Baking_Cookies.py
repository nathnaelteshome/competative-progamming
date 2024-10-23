n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

left, right = 0, 10**9

while left < right:
    mid = (left + right + 1) // 2
    required = 0
    for i in range(n):
        needed = a[i] * mid
        if needed > b[i]:
            required += needed - b[i]
        if required > k:
            break
    if required > k:
        right = mid - 1
    else:
        left = mid

print(left)
