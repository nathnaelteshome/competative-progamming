import heapq
from typing import List


class Custom:
    def __init__(self, distance, x, y):
        self.distance = distance
        self.x = x
        self.y = y

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))
        visit = set()
        ROWS, COLS = len(moveTime), len(moveTime[0])
        DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        print(minHeap)

        while minHeap:
                prevTime, row, col = heapq.heappop(minHeap)
                timeTaken = moveTime[row][col] + prevTime + 1
                visit.add((row, col))
                # print(minHeap, row, col, timeTaken, visit)

                if (row, col) == (ROWS - 1, COLS - 1):
                    return timeTaken

                for r, c in DIRECTION:
                    nr, nc = row + r, col + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                        heapq.heappush(minHeap, (timeTaken, row, col))
        
        return 0


soln = Solution()
print(soln.minTimeToReach([[0,4],[4,4]])) # Expected output: 7