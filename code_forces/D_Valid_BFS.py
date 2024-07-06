from collections import defaultdict, deque


n = int(input())
n = 4
# graph = list()

# graph = [set() for _ in range(n + 1)]

# for _ in range(n - 1):
#     u, v = [int(x) for x in input().split()]
#     graph[u].add(v)
#     graph[v].add(u)

graph = {1: {2, 3}, 2: {1, 4}, 3: {1}, 4: {2}}

# order = [int(x) for x in input().split()]
order = [1, 2, 3, 4]

ans = "Yes"

if order[0] != 1:
    ans = "No"

if ans == "Yes":
    i, j = 1, 0
    while i < n and j < n:
        if order[i] in graph[order[j]]:
            i += 1
        else:
            j += 1

    if i != n:
        ans = "No"
print(ans)
