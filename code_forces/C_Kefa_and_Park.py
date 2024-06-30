from collections import defaultdict


def areAllVisited(graph, visited):
    for vertex in graph:
        if vertex not in visited:
            return False
    return True


n, m = [int(x) for x in input().split()]
list_of_cats = [int(x) for x in input().split()]

graph = defaultdict(list)
stack = [[1, m, 0]]
visited = set([1])
res = 0

for i in range(m - 1):
    node1, node2 = [int(x) for x in input().split()]

    graph[node1].append(node2)
    graph[node2].append(node1)


while stack:
    cur = stack.pop()
    vertex = cur[0]
    cats = cur[1]
    level = cur[2]

    if areAllVisited(graph[vertex], visited) in visited and cats >= 0:
        if list_of_cats[vertex - 1] == 1:
            continue
        else:
            res += 1

    for neighbor in graph[vertex]:
        if neighbor not in visited and cats >= 0:
            if list_of_cats[vertex - 1] == 0:
                stack.append([neighbor, m, level + 1])

            else:
                stack.append([neighbor, cats - 1, level + 1])
            visited.add(neighbor)


print(res)
