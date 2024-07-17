from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = -1, len(arr)

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid

        return right


soln = Solution()
