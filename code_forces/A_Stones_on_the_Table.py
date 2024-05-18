no_of_stones = int(input())
# stones = input() #"RRG"
stones_str = str(input())
stones = [str(x) for x in stones_str] #['R', 'R', 'G']
ans = 0

for idx, val in enumerate(stones[1:]): #stones = ['R', 'G"]
    if val == stones[idx]:
        ans += 1

print(ans)

