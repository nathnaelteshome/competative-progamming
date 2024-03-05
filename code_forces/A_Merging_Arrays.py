n, m =[int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
ptr1 = 0
ptr2 = 0
result= []

while ptr1 < n and ptr2 < m:
    if arr1[ptr1] < arr2[ptr2]:
        result.append(arr1[ptr1])
        ptr1 += 1

    else:
        result.append(arr2[ptr2])
        ptr2 += 1

    
result += arr1[ptr1:] + arr2[ptr2:]

print(*result)



