class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictionary = {}
        new_num = list()

        for index, num in enumerate(nums):
            dictionary[num] = index

        for rem, ins in operations:
            index = dictionary[rem]
            dictionary.pop(rem)
            dictionary[ins] = index

        for key in dictionary:
            new_num.append(key)

        new_num.sort(key = lambda x: dictionary[x])

        return new_num
