def checkPossibility(nums):
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                num = nums[i]
                nums.pop(i)
                if nums == sorted(nums):
                    return True
                nums.insert(i,num)
                nums.pop(i-1)
                if nums == sorted(nums):
                    return True
                else:
                    return False

nums = [4,2,3]
print(checkPossibility(nums))