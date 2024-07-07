from collections import defaultdict, deque


n = int(input())
# n = 4
# graph = list()

graph = [set() for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = [int(x) for x in input().split()]
    graph[u].add(v)
    graph[v].add(u)

# graph = {1: {2, 3}, 2: {1, 4}, 3: {1}, 4: {2}}

order = [int(x) for x in input().split()]
# order = [1, 2, 4, 3]

ans = "Yes"

if order[0] != 1:
    ans = "No"

if ans == "Yes":
    child_idx, parent_idx = 1, 0
    while child_idx < n and parent_idx < n:
        if order[child_idx] in graph[order[parent_idx]]:
            child_idx += 1
        else:
            parent_idx += 1

    if child_idx != n:
        ans = "No"
print(ans)
