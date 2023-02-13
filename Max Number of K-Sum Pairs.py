class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        dictn = Counter(nums)
        for i in dictn:
            reverse = k-i
            if reverse == i:
                counter += int(dictn[i]/2)
            elif reverse in dictn and dictn[k-i] != 0 and dictn[i] != 0:
                minim = min(dictn[i], dictn[k-i])
                counter += minim
                dictn[i] -= minim
                dictn[k-i] -= minim

        return counter
