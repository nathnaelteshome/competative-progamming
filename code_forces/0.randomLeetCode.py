from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)

        print(graph)
        # defaultdict(<class 'list'>, {0: [1, 2], 2: [1, 3], 3: [1, 2, 4], 4: [2, 3]})

        def dfs(idx, visited):
            if idx in visited:
                return 0

            visited.add(idx)
            for neigh in graph[idx]:
                dfs(neigh, visited)
            return len(visited)

        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res


soln = Solution()
print(soln.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
