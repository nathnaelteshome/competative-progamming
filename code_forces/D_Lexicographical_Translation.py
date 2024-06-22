s = input()


def check(ch, count):
    for i in range(ord(ch) - ord("a")):
        if count[i]:
            return False

        return True


ans = []
stack = []
count = [0] * 26

for char in s:
    count[ord(char) - ord("a")] += 1

for i in range(len(s)):
    count[ord(s[i]) - ord("a")] -= 1
    stack.append(s[i])

    while stack and check(stack[-1], count):
        ans.append(stack.pop())

    answer = "".join(ans)
    print(answer)
