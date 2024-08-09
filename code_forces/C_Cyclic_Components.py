from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

candidates = set(v for v in range(1, n + 1) if len(graph[v]) == 2)
cycle_count = 0

while candidates:
    e = candidates.pop()
    left, right = graph[e]

    while left in candidates:
        candidates.remove(left)
        v1, v2 = graph[left]

        if v1 in candidates:
            left = v1
        elif v2 in candidates:
            left = v2
        else:
            break
        if left == right:
            cycle_count += 1
print(cycle_count)
