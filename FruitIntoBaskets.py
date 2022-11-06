from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        temp = left
        mx = 0
        k = 0

        while right <= (len(fruits)-1):

            if fruits[right] != fruits[temp] and k == 0:
                temp = right
                k = 1
            elif fruits[right] != fruits[temp] and fruits[right] != fruits[left]:
                left = temp
                right = temp
                k = 0

            mx = max(mx, right-left+1, right-temp+1)
            right += 1
        return mx


obj = Solution()
print(obj.totalFruit(fruits=[0, 0, 1, 1, 1, 2, 3, 3, 3, 3, 2]))
