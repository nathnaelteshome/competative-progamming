class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index, prev):
            if index == len(s):
                return True

            for j in range(index, len(s)):
                val = int(s[index : j + 1])
                if val + 1 == prev and backtrack(j + 1, val):
                    return True
                    print(val)
            return False

        for i in range(len(s) - 1):
            first_val = int(s[: i + 1])

            if backtrack(i + 1, first_val):
                return True

        return False


soln = Solution()
soln.splitString("050043")
