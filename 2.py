class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res
    
# typing master pro 7 how are we doing and thank you 