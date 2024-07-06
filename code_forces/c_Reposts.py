from collections import defaultdict, deque


n = int(input())
grpah = defaultdict(list)


for i in range(n):
    name1, repost, name2 = [str(x) for x in input().split()]
    # name1, repost, name2 = [x for x in sentence[i].split()]
    grpah[name2.lower()].append(name1.lower())

queue = deque(["polycarp"])
level = 0
visited = set()

while queue:
    level += 1
    for _ in range(len(queue)):
        curr = queue.popleft()

        for name in grpah[curr]:
            if name not in visited:
                visited.add(name)
                queue.append(name)

print(level)
