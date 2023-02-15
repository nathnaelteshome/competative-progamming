def reverseParentheses(s):
    if not s:
        return ''

    stack1 = []
    for char in s:
        if char == ')':
            word = ''
            while stack1 and stack1[-1] != '(':
                lastWord = stack1.pop()[::-1]
                word += lastWord
            stack1.pop()
            stack1.append(word)
        else:
            stack1.append(char)
    return "".join(stack1)


s = "(abcd)"
s = "(u(love)i)"
s = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s))
