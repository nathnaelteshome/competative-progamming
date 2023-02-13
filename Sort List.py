class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        # iterate the list
        node, l = head, [[head.val, head]]
        while node.next:
            node = node.next
            l.append([node.val, node])

        l.sort(key=lambda x: x[0])

        # reconstruct the list
        node = head = l[0][1]
        for k, v in l[1:]:
            node.next = v
            node = node.next
        node.next = None

        return head
