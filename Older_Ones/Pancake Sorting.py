class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        r = len(arr)
        l = 0
        res = []

        def reverse(initial, final):
            arr[:initial] = list(reversed(arr[:initial]))
            arr[:final] = list(reversed(arr[:final]))
        while l < r:
            for i in range(1, r):
                if arr[i] > arr[l]:
                    l = i
            reverse(l+1, r)
            res.append(l+1)
            res.append(r)
            r -= 1
            l = 0
        return res
