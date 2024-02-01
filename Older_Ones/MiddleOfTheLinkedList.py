from typing import Optional


class Solution:
    def __init__(self, x):
        self.val = x
        self.next = None

    def middleNode(self, head: Optional[ListNode]):
        nodeList = []
        while head != None:
            nodeList.append(head)
            head = head.next
        return nodeList[len(nodeList)//2]


obj = Solution()
print(obj.middleNode(head=[1, 2, 3, 4, 5]))
