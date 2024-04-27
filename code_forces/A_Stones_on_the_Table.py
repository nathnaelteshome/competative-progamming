input()
stones = input()
count = 0
previous_stone = None

for stone in stones:
    if previous_stone == stone:
        count += 1
    previous_stone = stone

print(count)