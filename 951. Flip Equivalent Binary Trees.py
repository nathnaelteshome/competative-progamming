from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(rootA, rootB):
            if not rootA or not rootB:
                return True

            leftA, rightA = rootA.left, rootA.right
            leftB, rightB = rootB.left, rootB.right


            if leftA.val == rightB.val and rightB.val == leftA.val:
                leftA, rightA = rightA, leftA

            if ( leftA.val == leftB.val ) and rightA.val == rightB.val and dfs(leftA, leftB) and dfs(rightA, rightB):
                return True

            return False
        
        return dfs(root1, root2)

        
        # Example usage:
if __name__ == "__main__":
  # Create trees for testing
  root1 = TreeNode(1)
  root1.left = TreeNode(2)
  root1.right = TreeNode(3)
  root1.left.left = TreeNode(4)
  root1.left.right = TreeNode(5)
  root1.right.left = TreeNode(6)
  root1.left.right.left = TreeNode(7)
  root1.left.right.right = TreeNode(8)

  root2 = TreeNode(1)
  root2.left = TreeNode(3)
  root2.right = TreeNode(2)
  root2.right.left = TreeNode(4)
  root2.right.right = TreeNode(5)
  root2.left.right = TreeNode(6)
  root2.right.right.left = TreeNode(8)
  root2.right.right.right = TreeNode(7)

  solution = Solution()
  print(solution.flipEquiv(root1, root2))  # Output: True