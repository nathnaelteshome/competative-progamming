from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
         
        def binary_search(left, right, target):
            # implementation
            mid = (right + left) // 2

            while left + 1 < right:
                if target <= arr[mid]:
                    right = mid
                else:
                    left = mid

                mid = (right + left) // 2

            return right

        N = len(arr)
        r = len(arr) - 1

        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1

        ans = r

        l = 0
        if r == 0:
            return 0
        while l  < len(arr)  and ( l == 0 or arr[l - 1] <=  arr[l]):
            left_bound = r - 1
            target = arr[l]
            r = binary_search(left_bound, len(arr), target)

            if l > 0 and arr[l - 1] > arr[l]:
                break
            ans = min(ans, r - l - 1)
            l += 1
        return ans


soln = Solution()
print(soln.findLengthOfShortestSubarray(arr=[10,13,17,21,15,15,9,17,22,22,13]))