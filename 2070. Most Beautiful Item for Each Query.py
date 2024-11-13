from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def binary_search(target) -> int:
            left, right = -1, len(prefix_sum)
            mid = (left + right) // 2

            while left + 1 < right:
                if target > prefix_sum[mid][0]:
                    left = mid
                else:
                    right = mid
                
                mid = (left + right )// 2
            # print(prefix_sum, left, right)
            return right

        items.sort(key=lambda k: k[0])
        # print(items)
        hashMap = {}
        max_beauty = 0

        # [[1, 2], [2, 4], [3, 2], [3, 5], [5, 6]] --- items sorted
        local_b = 0
        prefix_sum = []
        for price, beauty in items:
            local_b = max(beauty, local_b)
            while prefix_sum and prefix_sum[-1][0] == price:
                prefix_sum.pop()
            prefix_sum.append([price, local_b])
        
        # print(prefix_sum)

        # prefix [[1, 2], [2, 4], [3, 4], [3, 5], [5, 6]]
        #         [[1, 2], [2, 4], [3, 5], [5, 6]]
        ans = []

        for q in queries:
            beauty = binary_search(q)
            ans.append(beauty)
        
        return ans
            
soln = Solution()
print(soln.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))