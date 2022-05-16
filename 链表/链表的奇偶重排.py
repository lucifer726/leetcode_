class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
#
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self , head: ListNode) -> ListNode:
        # write code here
        if head == None:
            return head
        even = head.next
        odd = head
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
