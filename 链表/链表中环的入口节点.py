# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while True:
            if not (fast and fast.next): return
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break

        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
