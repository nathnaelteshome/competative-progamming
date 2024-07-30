import heapq

n, k = [int(x) for x in input().split()]

songs = []
for _ in range(n):
    t, b = map(int, input().split())
    songs.append((t, b))
songs.sort(reverse=True, key=lambda x: x[1])  # [[6, 8], [4, 7], [3, 6], [15, 1]]

minHeap = []
ans = 0
k_length = 0

for song in songs:
    length, beauty = song
    k_length += length

    heapq.heappush(minHeap, length)  # [6, 4 , 3]
    if len(minHeap) > k:
        k_length -= heapq.heappop(minHeap)
    ans = max(ans, k_length * beauty)

print(ans)
