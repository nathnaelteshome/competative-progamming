t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    all_eaten=0
    for candy in candies:
        all_eaten+= candy-min_eaten
    
    print(all_eaten)