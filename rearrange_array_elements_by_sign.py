class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive_list = [num for num in nums if num > 0]
        negative_list = [num for num in nums if num < 0]
        output = []
        
        for i in range(len(nums)//2):
            output.append(postive_list[i])
            output.append(negative_list[i])

        return output

        