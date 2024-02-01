class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                temp = nums[i]
                nums[i] = nums[zeros]
                nums[zeros] = temp
                zeros += 1
