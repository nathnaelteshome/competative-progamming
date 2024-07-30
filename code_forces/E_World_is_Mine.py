# 4 3 2 5 6 8 3 4
# sorted = 2 3 3 4 4 5 6 8

# 6 1 1 3 5 3 1
# sorted = 1 1 1 3 3 5 6

# alice = [2 3 4] , bob = [5 6 8]
# alice = [1, 3] , bob = [5,6]

import heapq
from typing import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    n = 11
    cakes = [int(x) for x in input().split()]
    # cakes = [6, 11, 6, 8, 7, 5, 3, 11, 2, 3, 5]  # 6 11 6 8 7 5 3 11 2 3 5
    hashMap = Counter(cakes)
    cake_count = []

    for cake, count in hashMap.items():
        cake_count.append((cake, count))
    cake_count.sort()  # [(1, 3), (3, 2), (5, 1), (6, 1]
    total_eaten_bob = 0
    bobs_cake_item = []

    for i in range(len(cake_count)):
        total_eaten_bob += cake_count[i][1]
        curr_alice_cake = i - len(bobs_cake_item)
        heapq.heappush(bobs_cake_item, -cake_count[i][1])
        if total_eaten_bob > curr_alice_cake:
            total_eaten_bob += heapq.heappop(bobs_cake_item)

    print(len(cake_count) - len(bobs_cake_item))
