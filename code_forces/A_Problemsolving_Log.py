t = int(input())
from collections import defaultdict

for _ in range(t):
    n = int(input())
    letter = input()
    ans = 0
    hashMap = defaultdict(int)

    for char in letter:
        hashMap[ord(char)] += 1

    for char, occurance in hashMap.items():
        if char <= occurance + ord("A") - 1:
            ans += 1

    print(ans)
