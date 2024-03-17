n = int(input())

for _ in range(n):
    s = str(input())
    words = [str(x) for x in s]
    left, right = 0, len(words)-1
    notSimilar = 0

    while left < right:
        if words[left] != words[right]:
            notSimilar += 1
        right -= 1
        left += 1
    
    print(notSimilar)


