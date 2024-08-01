n = int(input())
max_size = int(1e4 + 10)
ps = [0] * max_size


for _ in range(n):
    s, t, b = map(int, input().split())
    ps[s] += b
    ps[t + 1] -= b

result = 0
for i in range(1, max_size):
    ps[i] += ps[i - 1]
    result = max(result, ps[i])

print(result)
