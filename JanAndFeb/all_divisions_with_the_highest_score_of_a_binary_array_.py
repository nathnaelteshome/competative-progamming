class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        leftZeros = 0
        rightOnes = sum(nums)
        score = [[0, (leftZeros + rightOnes)]]

        for index in range(1, len(nums)):
            
            if nums[index - 1] == 0:
                leftZeros += 1
            if nums[index - 1] == 1:
                rightOnes -= 1

            newScore =  leftZeros + rightOnes
            print(score)
            while score and newScore >= score[-1][1]:
                score.pop()
            score.append([index, newScore])


        return [x[1] for x in score]

# [[0, 1]]
# [[1, 2]]
# [[1, 2], [2, 1]]
        