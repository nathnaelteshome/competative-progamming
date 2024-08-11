from collections import defaultdict, deque


def modified_chat_screenshots():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        graph = defaultdict(list)
        num_nodes, num_edges = map(int, input().split())
        incoming = defaultdict(int)

        for i in range(1, num_nodes + 1):
            incoming[i] = 0

        for _ in range(num_edges):
            edge_list = list(map(int, input().split()))
            for i in range(1, num_nodes - 1):
                source, destination = edge_list[i], edge_list[i + 1]
                graph[source].append(destination)
                incoming[destination] += 1

        queue = deque([])

        for i in incoming:
            if incoming[i] == 0:
                queue.append(i)

        order = []

        while queue:
            curr_node = queue.popleft()
            order.append(curr_node)

            for neighbor in graph[curr_node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != num_nodes:
            print("NO")
        else:
            print("YES")


modified_chat_screenshots()
