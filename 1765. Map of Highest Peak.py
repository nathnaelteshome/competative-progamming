from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        queue = deque([])
        result = [[0] * COLS for i in range(ROWS)]
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visit = set()
        print("result", result)

        for row in range(ROWS):
            for col in range(COLS):
                if isWater[row][col] == 1: #is water
                    queue.append((row, col))

        level = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                result[row][col] = level
                visit.add((row, col))

                for r, c in DIRECTIONS:
                    nr, nc = row + r, col + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                        queue.append((nr, nc))

                    
            level += 1

        return result



soln = Solution()
print(soln.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]]))