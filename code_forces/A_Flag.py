n, m = [int(x) for x in input().split()]


def isValid(n, m):
    prev = -1
    for _ in range(n):
        col = [int(x) for x in input()]

        if sum(col) != m * col[0] or prev == col[0]:
            return "NO"

        prev = col[0]

    return "YES"


print(isValid(n, m))
