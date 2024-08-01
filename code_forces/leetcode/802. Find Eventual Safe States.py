from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        output = []
        visit = set()
        is_safe = {}

        def dfs(i):
            if i in visit:
                return False
            if graph[i] == []:
                return True
            if i in is_safe:
                return is_safe[i]

            visit.add(i)
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    is_safe[i] = False
                    return False
            visit.remove(i)
            is_safe[i] = True

            return is_safe[i]

        for i in range(len(graph)):

            x = dfs(i)
            if dfs(i):
                output.append(i)

        return output


soln = Solution()
print(soln.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
