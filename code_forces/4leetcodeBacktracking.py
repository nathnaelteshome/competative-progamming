from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def backtrack(node, prefix_sum, prev):
            nonlocal path  # Declare path as a nonlocal variable
            if not node:
                return

            value = node.val + prev[-1]
            if value - targetSum in prefix_sum:
                path += prefix_sum[value - targetSum]

            prev.append(value)
            prefix_sum[value] += 1
            if node.left:
                backtrack(node.left, prefix_sum, prev.copy())
                prefix_sum[prev[-1]] -= 1

            if node.right:
                backtrack(node.right, prefix_sum, prev.copy())
                prefix_sum[prev[-1]] -= 1

        backtrack(root, prefix_sum, [0])
        return path


# [fun(10, [0]), fun(10, [0, 10]), fun(15, [0, 10]), fun(18, [0,10,15])]

soln = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

soln.pathSum(root, 8)
