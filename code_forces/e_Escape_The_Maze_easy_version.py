n = int(input())

for _ in range(n):

    def can_vlad():
        room, friends = [int(x) for x in input().split()]
        graph = [set() for _ in range(room + 1)]
        friends_visited = set()
        friends_visited.add([int(x) for x in input().split()])

        for _ in range(room - 1):
            u, v = [int(x) for x in input().split()]
            graph[u].add(v)
            graph[v].add(u)

        edges = {key for key, val in graph.values() if len(val) == 1}
        vlad_queue = set([1])
        vlad_visited = set([1])
        level = 0

        while vlad_queue:
            level += 1
            for _ in range(len(friends_visited)):
                cur = friends_visited.pop()
                for child in graph[cur]:
                    if child not in friends_visited:
                        friends_visited.add(graph[cur])

            for _ in range(vlad_queue):
                cur = vlad_queue.popleft()

                if cur in edges:
                    return "Yes"

                for child in graph[cur]:
                    if child not in friends_visited and child not in vlad_visited:
                        vlad_queue.add(child)
        return "No"

    print(can_vlad())
