from collections import defaultdict


n, m = [int(x) for x in input().split()]
adj_list = defaultdict(list)

for _ in range(m):
    nodeA, nodeB = [int(x) for x in input().split()]

    adj_list[nodeA].append(nodeB)
    adj_list[nodeB].append(nodeA)

for key, val in adj_list.items():


