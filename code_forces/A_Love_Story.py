n = int(input())
word = "codeforces"


for _ in range(n):
    s = str(input())
    count = 0

    for idx in range(len(word)):
        if s[idx] != word[idx]:
            # print(s[idx])
            count += 1

    print(count)