t = int(input())
for _ in range(t):
    n = int(input())
    postives = [int(x) for x in input().split()]
    set_ = set([i for i in range(1, n + 1)])
    previousVal = 0
    difficulty = 0

    for i in postives:
        if i - previousVal in set_:
            set_.remove(i - previousVal)
        else:
            difficulty = i - previousVal

        previousVal = i

    if len(set_) <= 2 and (difficulty == 0 or sum(set_) == difficulty):
        print("YES")
    else:
        print("NO")