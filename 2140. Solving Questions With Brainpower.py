from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [None] * n 

        def dfs(i):
            if i >= n: return float('-inf')
            if memo[i] is None:
                point,brainpower = questions[i]
                if i + brainpower + 1 < n:
                    memo[i] = max(dfs(i+1),point+dfs(i+brainpower+1))
                else:
                    memo[i] = max(dfs(i+1),point)
            return memo[i]

        return dfs(0)


soln = Solution()
print(soln.mostPoints([[3,1],[4,3],[44,1],[2,5],[25,5]]))