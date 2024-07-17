import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)
        # If heap size exceeds k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return the current kth largest element
        return self.minHeap[0]


soln = KthLargest(3, [4, 5, 8, 9, 10, 2, 3, 5, 6, 7, 8])
print(soln.add(3))
print(soln.add(5))
print(soln.add(10))
