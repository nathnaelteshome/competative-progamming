def count(pos):
    c = 0
    for i in range(n):
        c = max(c, abs(x[i] - pos) / v[i])
    return c


n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
l = 1
r = 1000000000
while abs(r - l) > 5e-7:
    mid = (l + r) / 2
    if count(mid - 4e-6) < count(mid + 4e-6):
        r = mid
    else:
        l = mid
print(count(r))
