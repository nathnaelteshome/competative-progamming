class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        high_priority = "ba" if y > x else "ab"
        low_priority = "ab" if y > x else "ba"
        max_score = y if y > x else x
        min_score = x if y > x else y

        res = 0
        stack = []

        for char in s:
            if stack and char == high_priority[1] and stack[-1] == high_priority[0]:
                stack.pop()
                res += max_score
            else:
                stack.append(char)

        new_stack = []
        for char in stack:
            if (
                char == low_priority[1]
                and new_stack
                and new_stack[-1] == low_priority[0]
            ):
                res += min_score
                new_stack.pop()
            else:
                new_stack.append(char)

        return res


soln = Solution()
print(soln.maximumGain("cdbcbbaaabab", 4, 5))  # 19
