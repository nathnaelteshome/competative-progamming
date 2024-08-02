import collections
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [[0, float("inf")]] * len(quiet)
        adj_list = collections.defaultdict(list)

        for rich, poor in richer:
            adj_list[poor].append(rich)

        def dfs(node):
            if ans[node][1] != float("inf"):
                return ans[node]
            ans[node] = [node, quiet[node]]

            for child in adj_list[node]:
                k = dfs(child)
                if k[1] < ans[node][1]:
                    ans[node] = k

            return ans[node]

            minimum = min(quiet[node], quiet[child])

        print(adj_list)
        for index in range(len(quiet)):
            if ans[index][1] == float("inf"):
                dfs(index)


# input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]

soln = Solution()
print(
    soln.loudAndRich(
        richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
        quiet=[3, 2, 5, 4, 6, 1, 7, 0],
    )
)
