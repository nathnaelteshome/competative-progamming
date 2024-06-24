from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = 0

        def backtrack(node, prev):
            if not node:
                return

            value = node.val
            if value - targetSum in prev:
                path += 1

            if node.left:
                prev.append(node.left)
                backtrack(node.left, prev)
                prev.pop()

            if node.right:
                prev.append(node.right)
                backtrack(node.right, prev)

        backtrack(root, [0])
        return path


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
