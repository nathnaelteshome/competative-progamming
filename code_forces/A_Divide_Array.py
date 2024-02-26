from collections import defaultdict


n = input().split()
hashMap = defaultdict(list)
arr = [int(x) for x in input().split()]
negativeCount = 0
postiveCount = 0

for i in arr:
    if i == 0:
        hashMap[0].append(i)
    elif i < 0:
        hashMap[-1].append(i)
        negativeCount += 1
    else:
        hashMap[1].append(i)
        postiveCount += 1

if postiveCount == 0:
    hashMap[1].append(hashMap[-1].pop())
    hashMap[1].append(hashMap[-1].pop())

if negativeCount % 2 == 0:
    hashMap[0].append(hashMap[-1].pop())

for i in [-1, 1, 0]:
    print(len(hashMap[i]), end = " ")
    for j in range(len(hashMap[i])):
        print(hashMap[i][j], end = "\n" if j == len(hashMap[i]) - 1 else " "  )
    
    



