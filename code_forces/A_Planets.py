from typing import Counter


t = int(input())

for _ in range(t):
    n, c = [int(x) for x in input().split()]
    planets = [int(x) for x in input().split()]

    planetPerOrbit = Counter(planets)
    ans = 0

    for key, count in planetPerOrbit.items():
        if count > c:
            ans += c
        else:
            ans += count

    print(ans)
