for _ in range(int(input())):
    n, m, k = map(int, input().split())
    sequence1, sequence2 = input().split(), input().split()
    frequency1, frequency2 = {}, {}

    for c in sequence2:
        frequency1[c] = frequency1.get(c, 0) + 1
        frequency2[c] = 0

    result, count = 0, 0

    for i, c in enumerate(sequence1):
        if c in frequency2:
            frequency2[c] += 1
            if frequency2[c] <= frequency1[c]:
                count += 1

        if i - m >= 0:
            if sequence1[i - m] in frequency2:
                frequency2[sequence1[i - m]] -= 1
                if frequency2[sequence1[i - m]] < frequency1[sequence1[i - m]]:
                    count -= 1

        if i >= m - 1:
            result += int(count >= k)

    print(str(result))
