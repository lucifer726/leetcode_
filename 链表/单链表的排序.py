# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 给定一个节点数为n的无序单链表，对其按升序排序。
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        # write code here
        tmp = []
        tmp.append(head.val)
        while head.next:
            head = head.next
            tmp.append(head.val)
        tmp.sort()
        result = ListNode(-1)
        temp = result
        for i in tmp:
            tt = ListNode(i)
            temp.next = tt
            temp = temp.next
        return result.next