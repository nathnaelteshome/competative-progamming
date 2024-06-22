testcase = int(input())

for i in range(testcase):
    a = 0
    b = 0
    word = input()
    for j in range(len(word)):
        if word[j] == "A":
            a += 1
        else:
            b += 1
    print("A" if a > b else "B")
