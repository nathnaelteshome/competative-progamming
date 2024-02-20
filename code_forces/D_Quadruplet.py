n, target = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

# [1,1,2,4]
def findFour(arr , n, target):
    auxilaryArr = []
    for i in range(n):
        for j in range(i + 1, n):
           auxilaryArr.append([arr[i] + arr[j], i ,j])
    
    auxilaryArr.sort(key= lambda x: x[0])
    l = 0
    r = len(auxilaryArr) - 1
    while l < r:
        if auxilaryArr[l][0] + auxilaryArr[r][0]== target:
            indices = [auxilaryArr[l][1] + 1, auxilaryArr[l][2] + 1, auxilaryArr[r][1] + 1, auxilaryArr[r][2] + 1]
            if len(set(indices)) == 4:
                for i in indices:
                    print(i, end=" ")
                return
        elif auxilaryArr[l][0] + auxilaryArr[r][0] < target:
            l += 1
        elif auxilaryArr[l][0] + auxilaryArr[r][0] > target:
            r -= 1
    print("IMPOSSIBLE")

    

findFour(arr, n, target)
    