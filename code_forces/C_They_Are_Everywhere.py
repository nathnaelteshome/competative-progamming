from collections import Counter, defaultdict

n = int(input())
s = input()
l = 0
check = set(s)
dic = defaultdict(int)
minValue = float("inf")

for r in range(n):
    dic[s[r]] += 1
    
    while dic[s[l]]-1 != 0:
        dic[s[l]] -= 1
        l += 1
        
    if len(dic) == len(check):
        minValue=min(minValue, r - l + 1)
        
print(minValue)