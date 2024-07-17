from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        curr = []

        def dfs(row, col):
            curr.append(board[row][col])
            if word[: len(curr)] != curr:
                curr.pop()
                return False
            if word[:] == curr:
                return True

            for dx, dy in directions:
                new_r = row + dx
                new_c = col + dy

                if (
                    0 <= new_r < len(board)
                    and 0 <= new_c < len(board[0])
                    and (new_r, new_c) not in visited
                ):
                    visited.add((new_r, new_c))
                    if dfs(new_r, new_c):
                        return True
                    visited.remove((new_r, new_c))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col):
                    return True


soln = Solution()
print(
    soln.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
)  # Output: true
