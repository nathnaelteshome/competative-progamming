import heapq

n = int(input())
potions = [int(x) for x in input().split()]
health = 0
minHeap = []

for potion in potions:
    health += potion
    heapq.heappush(minHeap, potion)

    while health < 0:
        health -= heapq.heappop(minHeap)
print(len(minHeap))
