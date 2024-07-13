t = int(input())

for _ in range(t):
    n = int(input())
    s = [x for x in input()]
    res = 0

    for idx, char in enumerate(s[:-1]):
        if int(s[idx]) != (s[idx + 1]):
            res += 1

    ans = "YES" if s.count("0") + res > s.count("1") else "NO"
    print(ans)
