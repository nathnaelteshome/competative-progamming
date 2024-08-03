from collections import defaultdict


# verices, edges = [int(x) for x in input().split()]

visited = set()
# adj_list = defaultdict(list)
# for _ in range(edges):
#     node1, node2 = [int(x) for x in input().split()]
#     adj_list[node1].append(node2)
#     adj_list[node2].append(node1)
# defaultdict(<class 'list'>, {1: [2], 2: [1], 3: [4, 5], 4: [3, 5], 5: [4, 3]})
# defaultdict(<class 'list'>, {1: [8, 12], 8: [1], 12: [1], 5: [11, 15], 11: [5, 9], 9: [11, 15], 15: [9, 5], 4: [13, 3, 14], 13: [4, 3], 3: [13, 4, 14], 10: [16, 7], 16: [10, 7], 7: [10, 16], 14: [3, 4], 17: [6], 6: [17]})
adj_list = {1: [2], 2: [1], 3: [4, 5], 4: [3, 5], 5: [4, 3]}


def find_cycle():
    ans = 0

    def dfs(node, prev):
        nonlocal ans
        visited.add(node)
        for child in adj_list[node]:
            if child == prev:
                continue
            if child in visited:
                return True
            if dfs(child, node):
                ans += 1
                return True

    for idx in adj_list.keys():
        if idx not in visited:
            dfs(idx, None)
    return ans


print(find_cycle())
