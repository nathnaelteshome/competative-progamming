n = str(input())
m = int(input())

prefixSum = [0] * len(n)
running_sum = 0

for idx in range(1, len(n)):
    if n[idx - 1] == n[idx]:
        prefixSum[idx - 1] = 1
    else:
        prefixSum[idx - 1] = 0

prefixSum = [0] + prefixSum

for idx, num in enumerate(prefixSum [1:]):
    running_sum += num
    prefixSum[idx + 1] = running_sum


for _ in range(m):
    l, r = [int(x) for x in input().split()]

    print (prefixSum[r - 1] - prefixSum[l - 1])

        
        