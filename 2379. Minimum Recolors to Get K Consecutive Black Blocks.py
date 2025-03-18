class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        no_white = window.count("W")
        min_operation = no_white

        print(window, no_white)

        left = 0
        for right in range(k, len(blocks)):
            if blocks[right] == "W":
                no_white += 1
            if blocks[left] == "W":
                no_white -= 1

            min_operation = min(min_operation, no_white)

        return min_operation


soln = Solution()
print(soln.minimumRecolors("WBWBBBW", 2))
