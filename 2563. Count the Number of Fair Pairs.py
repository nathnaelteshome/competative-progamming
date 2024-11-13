from typing import List


from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lower_binary_search(target) -> int:
            l, r = -1, len(nums)
            mid = (l + r) // 2

            while l + 1 < r:
                # implemnation
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid
                mid = (l + r) // 2
            return r
        
        def higher_binary_search(target) -> int:
            l, r = -1, len(nums)
            mid = (l + r) // 2

            while l + 1 < r:
                # implemnation
                if target >= nums[mid]:
                    l = mid
                else:
                    r = mid
                mid = (l + r) // 2
            return l
                


        nums.sort() #[0, 1, 4, 4, 5, 7]
        print(nums)
        pairs = list()
        ans = 0
        
        for idx, num in enumerate(nums):
            left_bound = lower_binary_search(lower - num) #(3)
            right_bound = higher_binary_search(upper - num) #(6)
            if right_bound < 0 or left_bound >= len(nums):
                continue
            print(left_bound, right_bound,num)
            for bound in range(left_bound, right_bound + 1):             
                pa = tuple(sorted((bound, num)))
                if pa not in pairs:
                    pairs.append(pa)

        print(pairs)
        return len(pairs)


soln = Solution()

print(soln.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
print(soln.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))