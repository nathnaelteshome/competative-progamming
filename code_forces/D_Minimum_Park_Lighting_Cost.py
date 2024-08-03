def backtrack(positions, lights, index):
    if len(lights) == index:
        for pos in positions:
            if pos > 0:
                return float("inf")
        return 0

    result = backtrack(positions, lights, index + 1)

    s, t, p, cost = lights[index]

    for i in range(s, t + 1):
        positions[i] -= p

    result = min(result, cost + backtrack(positions, lights, index + 1))

    for i in range(s, t + 1):
        positions[i] += p

    return result


def solve():
    n, m = map(int, input().split())
    max_len = 124

    positions = [0] * max_len

    for _ in range(n):
        s, t, c = map(int, input().split())
        positions[s] += c
        positions[t + 1] -= c

    for i in range(1, len(positions)):
        positions[i] += positions[i - 1]

    lights = [0] * m

    for i in range(m):
        lights[i] = list(map(int, input().split()))

    print(backtrack(positions, lights, 0))


solve()
