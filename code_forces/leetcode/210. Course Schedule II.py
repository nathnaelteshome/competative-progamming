from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs implementation
        # adj_list = defaultdict(list)
        # incoming = defaultdict(int)
        # queue, order = deque(), []

        # for course, preReq in prerequisites:
        #     adj_list[preReq].append(course)
        #     incoming[course] += 1
        # print(adj_list, incoming)
        # for course in range(numCourses):
        #     if incoming[course] == 0:
        #         queue.append(course)

        # while queue:
        #     course = queue.popleft()
        #     order.append(course)

        #     for neigh in adj_list[course]:
        #         incoming[neigh] -= 1
        #         if incoming[neigh] == 0:
        #             queue.append(neigh)

        # return order if len(order) == numCourses else []

        #dfs implementation
        adj_list = defaultdict(list)
        colors = defaultdict(int)

        order = []

        for course, preReq in prerequisites:
            adj_list[preReq].append(course)

        def topSort(node, colors, adj_list, order):
            if colors[node] == 1:
                return False

            colors[node] = 1
            for neigh in adj_list[node]:
                if colors[neigh] == 2:
                    continue
                if not topSort(neigh, colors, adj_list, order):
                    return False
            colors[node] = 2
            order.append(node)
            return True


        for node in range(numCourses):
            if colors[node] != 0:
                continue
            if not topSort(node, colors, adj_list, order):
                return []

        return reversed(order)


soln = Solution()
soln.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])



