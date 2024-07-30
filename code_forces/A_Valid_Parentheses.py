par = input()
stack = []

for char in par:
    if stack and stack[-1] == "(" and char == ")":
        stack.pop()
        continue
    stack.append(char)

print(len(par) - len(stack))
