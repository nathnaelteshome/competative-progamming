# n = int(input())
# entering = [int(x) for x in input().split()]
# exiting = [int(x) for x in input().split()]

n = 5
entering = [3,5,2,1,4]
exiting = [4,3,2,5,1]

def findOvertakingcar(n, entering, exiting):
    ans = 0

    exitMap = {}
    for idx, num in enumerate(exiting):
        exitMap[num] = idx

    overTaken = exitMap[entering[0]]

    for idx in range(1 ,n):
        exitIndx = exitMap[entering[idx]]
        if exitIndx - idx < overTaken:
            ans += 1
        overTaken = max(overTaken, exitIndx - idx)

    return overTaken

print(findOvertakingcar(n, entering, exiting))