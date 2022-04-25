class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def resverse(self, head: ListNode):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

    def isPail(self, head: ListNode) -> bool:
        # write code here
        if head == None:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.resverse(slow)
        fast = head
        while slow:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next
        return True