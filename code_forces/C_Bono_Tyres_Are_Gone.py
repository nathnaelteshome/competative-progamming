n = int(input())
stack = []
rearrange = 0

for _ in range(2 * n):
    command = input().split()
    if command[0][0] == "a":
        stack.append(int(command[1]))
    else:
        sortedStack = sorted(stack, reverse=True)
        if stack and stack != sortedStack:
            stack = sortedStack
            rearrange += 1
        stack.pop()

print(rearrange)
