from collections import defaultdict
t = int(input())

for i in range(t):
    num_lanterns = int(input())
    lanterns = defaultdict(list)
    score = 0 

    for i in range(num_lanterns):
        threshold, prize = list(map(int, input().split()))

        lanterns[threshold].append(prize)
    for threshold in lanterns:
        turned_on_laterns = sorted(lanterns[threshold], reverse=True)[:threshold]
        score += sum(turned_on_laterns)
    
    print(score)
