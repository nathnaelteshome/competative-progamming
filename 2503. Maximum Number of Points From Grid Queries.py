from heapq import heappush
import heapq
from queue import PriorityQueue
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        result = [0] * len(queries)
        # Directions for movement (right, down, left, up)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Store queries along with their original indices to restore order
        # later
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        # Min-heap (priority queue) to process cells in increasing order of
        # value
        min_heap = []
        visited = [[False] * COLS for _ in range(ROWS)]
        # Keeps track of the number of cells processed
        total_points = 0
        # Start from the top-left cell
        heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = True

        # Process queries in sorted order
        for query_value, query_index in sorted_queries:
            # Expand the cells that are smaller than the current query value
            print(min_heap)
            while min_heap and min_heap[0][0] < query_value:
                cellValue, current_row, current_col = min_heap[0]

                # Increment count of valid cells
                total_points += 1

                # Explore all four possible directions
                for dr, dc in DIRECTIONS:
                    nr, nc = (
                        current_row + dr,
                        current_col + dc,
                    )

                    # Check if the new cell is within bounds and not visited
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        not visited[nr][nc]
                    ):
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        # Mark as visited
                        visited[nr][nc] = True
            # Store the result for this query
            result[query_index] = total_points

        return result

from collections import defaultdict, deque
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def find_points():
            out = 0
            for key, val in visit.items():
                out += len(val)
            return out

        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = defaultdict(list)
        ROWS, COLS = len(grid), len(grid[0])
        queries.sort()
        visit[0].append((0, 0))
        ans = []


        for q in queries:
            if q <= grid[0][0]:
                ans.append(0)
                continue
            
            level = max(visit.keys())
            queue = deque(visit[level])

            while queue:
                level += 1

                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            if grid[nr][nc] < q:
                                queue.append((nr, nc))
                            visit[level].append((nr, nc))
            
            points = find_points()
            ans.append(points)
        
        return ans


soln = Solution()
print(soln.maxPoints(grid =
[[1,2,3],[2,5,7],[3,5,1]], queries=[5,6,2])) # [14,13,13,13,13]