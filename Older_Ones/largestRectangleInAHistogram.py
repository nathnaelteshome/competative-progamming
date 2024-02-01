from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    # stack, mx = [], 0
    # # for index ,height loop
    # for i, h in enumerate(heights + [0]):
    #     while stack and heights[stack[-1]] > h:
    #         H = heights[stack.pop()]
    #         if not stack:
    #             W = i
    #         else:
    #             W = i-stack[-1]-1
    #         mx = max(mx, H*W)
    #     stack.append(i)

    # return mx

    maximum = 0
    stack = []

    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            H = heights[heights.pop()]
            if not stack:
                W = i
            else:
                W = i-stack[-1]-1
            maximum = (maximum, H*W)

        stack.append(i)
    return maximum


largestRectangleArea(heights=[1, 2, 3, 1, 5, 6, 2, 3])
