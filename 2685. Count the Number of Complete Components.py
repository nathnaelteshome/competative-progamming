from typing import DefaultDict, List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = DefaultDict(list)  # {0 : [1, 2] ...}
        visit = set()
        res = 0

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        def dfs(v, res):
            if v in visit:
                return
            visit.add(v)
            res.append(v)

            for nei in adj_list[v]:
                dfs(nei, res)
            return res

        for v in range(n):
            if v not in visit:
               component = dfs(v, [])
                if all(len(component) - 1 == len(adj_list[v2]) for v2 in component):
                    res += 1

        return res


soln = Solution()
print(soln.countCompleteComponents(6,[[0, 1], [0, 2], [1, 2], [3, 4]]))
