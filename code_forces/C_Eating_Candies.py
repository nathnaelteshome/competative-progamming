t = int(input())

for _ in range(t):
    n = int(input())
    candies = [int(x) for x in input().split()]  # [1, 2, 3, 4, 5]
    prefix_sum = [0] * (n + 1)
    suffix_sum = [0] * (n + 1)

    for idx in range(n):
        prefix_sum[idx + 1] = candies[idx] + prefix_sum[idx]  # [0., 3, 6, 10, 15]
        suffix_sum[n - idx - 1] = (
            candies[n - idx - 1] + suffix_sum[n - idx]
        )  # [15, 14 12, 9, 5, 0]

    suffix_sum[::-1]
    prefix_sum = prefix_sum[1:]
    suffix_sum = suffix_sum[:n]

    left = 0
    right = n - 1
    ans = 0

    while left < right:
        if prefix_sum[left] == suffix_sum[right]:
            ans = (left + 1) + (n - right)
            left += 1
            right -= 1
        elif prefix_sum[left] < suffix_sum[right]:
            left += 1
        else:
            right -= 1

    print(ans)
