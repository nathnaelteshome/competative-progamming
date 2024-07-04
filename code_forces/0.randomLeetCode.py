class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        stack = []

        def backTrack(idx):
            # if stack has 3 numbers in it and they add up to give the last
            if len(stack) > 2 and not stack[-1] == stack[-2] + stack[-3]:
                return

            # base case if we reach the end of num and all is good
            if idx == len(num) and len(stack) > 2:
                return True

            for i in range(idx, len(num)):
                # section
                section = num[idx : i + 1]

                # checking is section doesnt have a leading 0
                if len(section) > 1 and section[0] == "0":
                    continue

                stack.append(int(section))
                if backTrack(i + 1):
                    return True
                stack.pop()

        return backTrack(0)


soln = Solution()
print(soln.isAdditiveNumber("112358"))
