class Solution:
    def deleteDuplicates(self, head):
        curr = head
        while curr != None:
            if curr.next == None:
                break
            else:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
        return head
