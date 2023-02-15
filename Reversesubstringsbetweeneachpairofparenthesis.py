import string


def solution(s: string):
    stack = []
    for char in s:
        if str(char) != ")":
            stack.append(str(char))
        else:
            k = stack.pop()
            temp = ""
            while k != "(":
                temp += k
                k = stack.pop()

            stack.append(temp[::-1])

    if len(stack) != 1:
        temp = ""
        while len(stack) > 0:
            temp += stack.pop()
        stack.append(temp)

    return stack.pop()[::-1]


s = "(abcd)"
s = "(u(love)i)"
# s = "a(bcdefghijkl(mno)p)q"

print(solution(s))
