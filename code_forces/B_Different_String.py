testcase = int(input())


for i in range(testcase):
    word = input()
    first = word[0]
    swappable = False

    for j in range(1, len(word)):
        if word[j] != first:
            if j < len(word) - 1:
                word = word[j] + word[1:j] + word[0] + word[j + 1 :]
            else:
                word = word[j] + word[1:j] + word[0]
            swappable = True
            break

    if swappable == True:
        print("Yes")
        print(word)
    else:
        print("No")
