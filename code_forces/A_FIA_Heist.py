s = str(input())
stack = []
idx = 0
sList = [str(x) for x in s]
# print(ans)

while idx < len(sList):
    if sList[idx].isalpha() or sList[idx] in ".,?" or sList[idx] == " ":
        stack.append(sList[idx])

    elif stack and sList[idx] == "<":
        stack.pop()
    idx += 1
    
print("".join(stack))

    
        