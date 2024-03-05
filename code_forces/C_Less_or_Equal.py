def lessOrEqual(k, nums):
    if k == 0:
        if nums[0] == 1:
            print(-1)
        else:
            print(1)
        return
    
    if k  == n or nums[k] - nums[k - 1]:
        print(nums[k - 1])
    else:
        print(-1)
        
 
n, k = [int(x) for x in input().split()] 
nums = [int(x) for x in input().split()] 
 
nums.sort()

 
lessOrEqual(k, nums)
 
 
 