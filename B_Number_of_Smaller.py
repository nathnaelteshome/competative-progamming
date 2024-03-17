n, k = [int(x) for x in input().split()] 
nums1 = [int(x) for x in input().split()] 
nums2 = [int(x) for x in input().split()] 

count, second = 0, 0
result = [] 

for idx, num in enumerate(nums2):
    while second < len(nums1) and nums1[second] < num:
        count += 1
        second += 1
    result.append(count)

print(*result)