def isValid(s):
    opening = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            opening.append(i)
        elif i == ')' or i == '}' or i == ']':
            if len(opening) == 0:
                return False
            poped = opening.pop(-1)
            if i == ')' and poped == '(':
                ans = True
            elif i == '}' and poped == '{':
                ans = True
            elif i == ']' and poped == '[':
                ans = True
            else:
                return False
        else:
            return False
    if len(opening) != 0:
        ans = False
    return ans


# print(isValid("([]){"))
