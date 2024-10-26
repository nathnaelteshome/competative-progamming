import unittest
from remove_sub_folders import Solution

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_removeSubfolders(self):
    self.assertEqual(
      self.solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]),
      ["/a", "/c/d", "/c/f"]
    )
    self.assertEqual(
      self.solution.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]),
      ["/a"]
    )
    self.assertEqual(
      self.solution.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]),
      ["/a/b/c", "/a/b/ca", "/a/b/d"]
    )

if __name__ == '__main__':
  unittest.main()