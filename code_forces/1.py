def findOvertakingcar(n, entering, exiting):
    ans = 0

    exitMap = {}
    for idx, num in enumerate(exiting):
        exitMap[num] = idx

    overTaken = exitMap[entering[0]]
    print(exitMap)

    for idx in range(1 ,n):
        if entering[idx] + overTaken > exitMap[entering[idx]]:
            ans += 1
        overTaken = max(overTaken, exitMap[entering[idx]] - idx)

    return ans
    
n = 5
entering = [3,5,2,1,4]
exiting = [4,3,2,5,1]


print(findOvertakingcar(n, entering, exiting))