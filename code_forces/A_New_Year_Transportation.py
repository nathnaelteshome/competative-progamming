n, t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

step = 1

while step < t:
    step += a[step - 1]
    if step >= t:
        break

if step == t:
    print("YES")
else:
    print("NO")
