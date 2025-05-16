class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) / 3
        dictionary = Counter(nums)
        output = []
        
        for key, value in dictionary.items():
            if value > n:
                output.append(key)
        
        return output

        