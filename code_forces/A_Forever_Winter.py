from collections import Counter, defaultdict


t = int(input())

for _ in range(t):
    graph = defaultdict(list)
    n, m = [int(x) for x in input().split()]

    for _ in range(m):
        node1, node2 = [int(x) for x in input().split()]
        graph[node1].append(node2)
        graph[node2].append(node1)

    # print(graph)
    all_vertices = list(graph.values())
    all_vertices.sort(key=len)
    count = defaultdict(int)

    for vertice in all_vertices:
        if len(vertice) == 1:
            continue
        else:
            count[len(vertice)] += 1
    ans = list(count.items())
    # sort by values
    ans.sort(key=lambda x: x[1])
    x, y = ans[0][0], ans[-1][0]
    print(x, y - 1)

    # print(f"{x} {y}")
