from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Approch
        """
        using dfs
        create a backtrack function with two state the (no_of_queen & list of canidate moves)
        base case when we have all queens place
        for each canidate move we loop
        backtrack next queen with all the possible moves
        make a get possible moves function
        possible moves are all the areas that are not on the same col row and diag
        """
        result = []
        possibleMoves = set()
        final_ans = []
        visited = set()
        ans = []

        for row in range(n):
            for col in range(n):
                possibleMoves.add((row, col))

        def getPossibleMoves(canidate, canidates):
            new_canidates = canidates.copy()
            blocked_moves = []
            for i in range(n):
                blocked_moves.append((canidate[0] - i, canidate[1]))
                blocked_moves.append((canidate[0] + i, canidate[1]))
                blocked_moves.append((canidate[0], canidate[1] + i))
                blocked_moves.append((canidate[0], canidate[1] - i))
                blocked_moves.append((canidate[0] - i, canidate[1] - i))
                blocked_moves.append((canidate[0] + i, canidate[1] + i))
                blocked_moves.append((canidate[0] - i, canidate[1] + i))
                blocked_moves.append((canidate[0] + i, canidate[1] - i))

            for blocked_move in blocked_moves:
                if blocked_move in new_canidates:
                    new_canidates.remove(blocked_move)

            return new_canidates

        def backtrack(n, canidates):
            if n == 0:
                return True

            for canidate in canidates:
                result.append(canidate)
                if (
                    backtrack(n - 1, getPossibleMoves(canidate, canidates))
                    and set(result) not in visited
                ):
                    final_ans.append(result.copy())
                    visited.add(set(result.copy()))
                result.pop()

        backtrack(n, possibleMoves)

        for positions in final_ans:
            single_ans = []
            for row in range(n):
                row_val = ""
                for col in range(n):
                    if (row, col) in positions:
                        row_val += "Q"
                    else:
                        row_val += "."

                single_ans.append(row_val)
            ans.append(single_ans)

        return ans


soln = Solution()
print(soln.solveNQueens(4))
