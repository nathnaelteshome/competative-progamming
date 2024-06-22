n = int(input())
word = list(str(input()))
l = 0
res = 1

for r in range(1, n):
    if ord(word[r - 1]) + 1 != ord(word[r]):
        res = max(res, r - l)
        l = r
    if r == n - 1:
        res = max(res, r - l + 1)

print(res)





