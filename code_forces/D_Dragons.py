s, n = map(int, input().split())
for i, j in sorted(list(map(int, input().split())) for i in " " * n):
    s = (s + j) * (s > i)
print("YNEOS"[s < 1 :: 2])
