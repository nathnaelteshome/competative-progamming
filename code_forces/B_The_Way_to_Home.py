from collections import deque


n, d = [int(x) for x in input().split()]
# n, d = [4, 2]
lili = input()
# lili = "1001"
s = [int(x) for x in lili]


def shortPath(n, d, s):
    if s[0] == 0 or s[n - 1] == 0:
        return -1

    if n == 1:
        return 0
    # bfs approch
    visited = set()

    queue = deque([0])
    level = 0

    while queue:
        level += 1
        for _ in range(len(queue)):
            curr = queue.popleft()

            for i in range(curr + 1, min(len(s), n + 1, curr + d + 1)):
                if s[i] == 1 and i not in visited:
                    if i == n - 1:
                        return level
                    queue.append(i)
                    visited.add(i)

    return -1


print(shortPath(n, d, s))
