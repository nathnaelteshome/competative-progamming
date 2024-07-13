import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, t in enumerate(tasks):
            t.append(idx)

        tasks.sort(key=lambda t: t[0])
        # tasks = [[1, 2, 0], [2, 4, 1], [3, 2, 2] ....]
        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minHeap:
                time = tasks[i][0]

            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)

        return res


soln = Solution()
print(soln.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))  # [0, 2, 3, 1]
