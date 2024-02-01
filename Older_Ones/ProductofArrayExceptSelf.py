from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        output = [1]
        for i in range(len(nums)-1, 0, -1):
            output.append(output[-1]*nums[i])
        output.reverse()
        for i in range(len(nums)):
            output[i] = output[i]*left
            left *= nums[i]
        return output


# obj = Solution()
# print(obj.productExceptSelf(nums=[1, 2, 3, 4]))
