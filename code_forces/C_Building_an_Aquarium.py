t = int(input())

for _ in range(t):
    n, x = [int(x) for x in input().split()]
    corals = [int(x) for x in input().split()]
    heigh_diff = [0] * (n)
    idx = 0

    maxHeight = max(corals)
    h = maxHeight

    def calculate_water(h, corals):
        water = 0
        for idx, coral in enumerate(corals):
            if coral < h:
                water += h - coral
                heigh_diff[idx] = h - coral

        return water

    water_capacity = calculate_water(h, corals)

    if water_capacity == x:
        continue

    elif water_capacity > x:
        heigh_diff.sort()
        while water_capacity > x and h > 0:
            h -= 1
            while idx <= len(heigh_diff) and heigh_diff[idx] == 0:
                idx += 1
            right = idx
            while right < len(heigh_diff):
                heigh_diff[right] -= 1
                right += 1
            water_capacity -= len(heigh_diff) - idx

    else:
        h += (x - water_capacity) // n

    print(h)
