# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
import math
class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        dummyNode = listNode(-1)
        dummyNode.next = head
        pre = dummyNode
        length = 0
        while head:
            length += 1
            head = head.next
        sonNum = math.floor(length/k)
        for _ in range(sonNum):
            cur = pre.next
            cur_next = ListNode(-1)
            for i in range(k - 1):
                cur_next = cur.next
                cur.next = cur.next.next
                cur_next.next = pre.next
                pre.next = cur_next
            pre = cur
        return dummyNode.next
