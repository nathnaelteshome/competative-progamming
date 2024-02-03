class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        output = 0
        for repetition in count.values():
            good_pairs = repetition * (repetition - 1) // 2
            output += good_pairs
        return output