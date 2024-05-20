n, t = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]

left = 0
maximum = 0

for right in range(n):
    t -= time[right]
    while t < 0:
        t += time[left]
        left += 1

    maximum = max(maximum, right - left + 1)

print(maximum)
