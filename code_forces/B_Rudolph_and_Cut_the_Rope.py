t = int(input())
for _ in range(t):
    n = int(input())
    hang_length = []
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        if a - b > 0:
            hang_length.append(a - b)

    print(len(hang_length))
