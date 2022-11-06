class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        position = []
        for i, num in enumerate(nums):
            if num == target:
                position.append(i)

        return position
