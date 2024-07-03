class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        stack = []

        def backTrack(idx):
            if len(stack) > 2 and not stack[-1] == stack[-2] + stack[-3]:
                return

            if idx == len(num) and len(stack) > 2:
                return True

            for i in range(idx, len(num)):
                first_num = num[idx : i + 1]

                if len(first_num) > 1 and first_num[0] == "0":
                    continue

                stack.append(int(first_num))
                if backTrack(i + 1):
                    return True
                stack.pop()

        return backTrack(0)


soln = Solution()
print(soln.isAdditiveNumber("112358"))
