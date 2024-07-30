import bisect

for _ in range(int(input())):
    n = int(input())
    portals = []
    for _ in range(n):
        start, end, min_value, max_value = map(int, input().split())
        portals.append([start, max_value])

    input()
    queries = list(map(int, input().split()))

    portals.sort()

    left = portals[0][0]
    right = portals[0][1]
    res = [[left, right]]

    for idx in range(1, n):
        if portals[idx][0] <= right:
            right = max(right, portals[idx][1])
            res[-1] = [left, right]
        else:
            res.append(portals[idx])
            left = portals[idx][0]
            right = portals[idx][1]

    ans = []

    for query in queries:
        index = bisect.bisect_right(res, [query, 10**18])

        if not index:
            ans.append(query)
        else:
            ans.append(max(query, res[index - 1][1]))

    print(*ans)
