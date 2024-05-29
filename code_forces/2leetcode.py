import math
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True

            if lower >= node.val or node.val >= upper:
                return False

            else:
                return helper(node.left, lower, node.val) and helper(
                    node.right, node.val, upper
                )

        return helper(root)


root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)


soln = Solution()

print(soln.isValidBST(root))
