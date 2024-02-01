class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        rep = {}
        num = 0
        for index in nums:
            if index in rep:

                if rep[index] == 1:
                    num += 1
                else:
                    num += rep[index]

                rep[index] += 1
            else:
                rep[index] = 1
        return num
