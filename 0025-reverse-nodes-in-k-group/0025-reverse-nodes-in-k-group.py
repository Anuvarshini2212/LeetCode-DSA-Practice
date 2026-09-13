class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next

            prev, curr = next_group, prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
