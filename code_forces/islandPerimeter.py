from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        perimeter = 0
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        # '''recursive approch'''

        def dfs(row, col):
            # base case if not land or out of bound:
            nonlocal perimeter
            if (
                row >= len(grid)
                or col >= len(grid[0])
                or col < 0
                or row < 0
                or grid[row][col] == 0
            ):
                return 1

            if (row, col) in visited:
                return 0

            visited.add((row, col))
            perimeter = (
                dfs(row + 1, col)
                + dfs(row, col + 1)
                + dfs(row - 1, col)
                + dfs(row, col - 1)
            )
            return perimeter

        dfs(0, 1)


soln = Solution()
soln.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
