n, target = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

[1,1,2,4]
def findFour(arr , n, target):
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        print(i + 1, j + 1, k + 1, l + 1)
                        return
                        # break
                    
    print("IMPOSSIBLE")
    

findFour(arr, n, target)
    



# arr.sort()
# window = arr[:4]
# summation = sum(window)
# if summation == target:
#         for i in arr:
#             print(i,end=" ")
        
# l, r  =  0, 4
# print(arr, window)
# while r < n:
#     summation -= arr[l]
#     summation += arr[r]
#     l += 1
#     r += 1
#     if summation == target:
#         for i in arr:
#             print(i,end=" ")
#         break


