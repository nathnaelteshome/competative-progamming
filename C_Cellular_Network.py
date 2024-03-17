# n, m = [int(x) for x in input().split()] 
# cities = [int(x) for x in input().split()] 
# towers = [int(x) for x in input().split()] 
# result = [] #[1, 2, 3, 4]

 
# for city in cities:
#     nearest = min([abs(city - tower) for tower in towers])
#     result.append(nearest)
 
# ans = max(result)
# print(ans)


n, m = [int(x) for x in input().split()] 
cities = [int(x) for x in input().split()] 
towers = [int(x) for x in input().split()] 
cities.sort()
towers.sort()
idx = 0
maxDistance = 0

for city in cities:
    while idx < len(towers) - 1 and towers[idx] - city <= 0:
        idx += 1

    minimum = abs(city - towers[idx - 1])

    nearest = min(minimum, abs(towers[idx] - city))
    maxDistance = max(maxDistance, nearest)

print(maxDistance)

