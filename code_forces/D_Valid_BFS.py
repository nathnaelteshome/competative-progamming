n = int(input())

# create the graph
n = int(input())
graph = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = [int(x) for x in input().split()]
    graph[u].add(v)
    graph[v].add(u)

order = [int(x) for x in input().split()]
# graph = {1: {2, 3}, 2: {1, 4}, 3: {1}, 4: {2}}


def valid_bfs():
    # order = [1, 2, 4, 3]

    if order[0] != 1:

        return "No"

    child_idx, parent_idx = 1, 0
    while child_idx < n and parent_idx < n:
        if order[child_idx] in graph[order[parent_idx]]:
            child_idx += 1
        else:
            parent_idx += 1

    if child_idx != n:
        return "No"

    return "Yes"


print(valid_bfs())
