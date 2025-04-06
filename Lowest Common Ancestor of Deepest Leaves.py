from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]

def build_tree(vals):
  if not vals:
    return None
  root = TreeNode(vals[0])
  queue = deque([root])
  i = 1
  while i < len(vals):
    node = queue.popleft()
    if i < len(vals) and vals[i] is not None:
      node.left = TreeNode(vals[i])
      queue.append(node.left)
    i += 1
    if i < len(vals) and vals[i] is not None:
      node.right = TreeNode(vals[i])
      queue.append(node.right)
    i += 1
  return root

soln = Solution()
tree = build_tree([3,5,1,6,2,0,8,None,None,7,4])
print(soln.lcaDeepestLeaves(tree).val)