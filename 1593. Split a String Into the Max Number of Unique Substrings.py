class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def backtrack(start):
            if start == len(s):
                return 0

            maxCount = 0

            for end in range(start + 1, len(s) + 1):
                word = s[start: end]
                if word not in seen:
                    seen.add(word)
                    maxCount = max(maxCount, 1 + backtrack(end))
                    seen.remove(word)
                    
            return maxCount

        return backtrack(0)

soln = Solution()
soln.maxUniqueSplit(s = "ababccc")
        
