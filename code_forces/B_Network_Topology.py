from collections import defaultdict


n, m = [int(x) for x in input().split()]
adj_list = defaultdict(list)

for _ in range(m):
    nodeA, nodeB = [int(x) for x in input().split()]

    adj_list[nodeA].append(nodeB)
    adj_list[nodeB].append(nodeA)

values = sorted(adj_list.values(), key=lambda x: len(x), reverse=True)
edges = []
if all(val == values[1] for val in values[1:]) and len(values[0]) == n - 1:
    print("star topology")
elif all(len(val) == 2 for val in values):
    print("ring topology")
elif (
    sum(len(val) == 1 for val in values) == 2
    and sum(len(val) == 2 for val in values) == n - 2
):
    print("bus topology")
else:
    print("unknown topology")
