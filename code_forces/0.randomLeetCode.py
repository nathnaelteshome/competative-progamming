from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        graph = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].append(bus)

        # print(graph)

        if source == target:
            return 0

        queue = deque([source])
        buses_taken = set()
        visited = set()
        level = 0

        while queue:
            level += 1

            for _ in range(len(queue)):
                curr = queue.popleft()
                for bus in graph[curr]:
                    if bus in buses_taken:
                        continue

                    buses_taken.add(bus)

                    for next_stop in routes[bus]:
                        if next_stop in visited:
                            continue

                        if next_stop == target:
                            return level

                        queue.append(next_stop)
                        visited.add(next_stop)

        return -1


soln = Solution()
print(soln.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
