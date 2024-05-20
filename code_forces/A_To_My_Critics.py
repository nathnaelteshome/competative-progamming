t = int(input())

for _ in range(t):
    a, b, c = [int(x) for x in input().split()]

    if (a + b >= 10) or (a + c >= 10) or (b >= 5 and c >= 5):
        print("YES")
    else:
        print("NO")
