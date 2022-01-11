# 给你一个链表的头节点 head ，判断链表中是否有环。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


head = [3,2,0,-4]
pos = 1
a = Solution()
print(a.hasCycle(ListNode(head)))