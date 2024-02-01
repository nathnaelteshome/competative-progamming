from typing import List


class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = k-1
        mx = 0
        max1 = 0

        if left >= -1*k:
            choppedCard = sum(cardPoints[left:right+1])
            max1 = choppedCard
            while right >= 0:
                left -= 1
                choppedCard -= cardPoints[right]
                choppedCard += cardPoints[left]
                right -= 1

                max1 = max(mx, max1, choppedCard)

        return max1


# obj = Solution()
# print(obj.maxScore(cardPoints=[11, 49, 100, 20, 86, 29, 72], k=4))
