# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        node = head
        node1 = head
#         computng the size of the linkedlist
        while node:
            node = node.next
            cnt += 1
# checking if size is 1 then return head with next value None
        if cnt == 1:
            head = None
            return head

        i = 1
        k = cnt-n
# if n equals to the size then chnge head to the next value of the head
        if n == cnt:
            head = head.next
            return head
# setting the pointer just before the node which has to be deleted
        while i < k:
            node1 = node1.next
            i += 1
# checking whether to be deleted node is last node or not
        if node1.next.next:
            node1.next = node1.next.next
        else:
            node1.next = None

        return head
