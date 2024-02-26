from collections import defaultdict


def FiraolsContest(diffculty, n , arr):
    result = ""
    checker = [0] * (diffculty + 1)
    hashMap = defaultdict(int)
    # total = diffculty
    
    for i in arr:
        # hashMap[i] += 1
        checker[i ] += 1
        hashMap[checker[i]] += 1
        if hashMap[checker[i]] == diffculty:
            result += "1"
        else:
            result += "0"
    print(result)
    return



diffculty, n = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

FiraolsContest(diffculty, n , arr)