# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(0)
        cur = new_node
        cur1 = l1
        cur2 = l2
        reminder = 0

        while cur1 and cur2:
            summ = cur1.val + cur2.val
            if summ > 9:
                summ = summ % 9
                new_node.val = summ + reminder
                reminder = 1
            else:
                new_node.val = summ + reminder
                reminder = 0
                
            new_node.next = ListNode()  # Create a new node for the next element
            new_node = new_node.next  # Move the current node pointer to the next node
            if cur1.next and cur2.next:
                cur1 = cur1.next
                cur2 = cur2.next
            else:
                if reminder:
                    new_node.val = reminder
                    new_node.next = None
                break
            