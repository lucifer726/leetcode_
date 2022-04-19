class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
# 给定两个这种链表，请生成代表两个整数相加值的结果链表。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    '''
    从最低位至最高位，逐位相加，如果和大于等于 10，则保留个位数字，同时向前一位进 1 如果最高位有进位，则需在最前面补 1。

    做有关链表的题目，有个常用技巧：添加一个虚拟头结点（哨兵），帮助简化边界情况的判断。

    一些细节：由于给定的两个数值是按照「从高位到低位」进行存储，但我们的计算过程是「从低位到高位」进行，
    因此在进行计算前，应当先对链表进行翻转。同时，在计算完成后，再对答案链表进行。
    '''
    def resverse(self, root: ListNode) -> ListNode:
        prev = None
        cur = root
        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def addInList(self, head1: ListNode, head2: ListNode) -> ListNode:
        # write code here
        l1, l2 = ListNode(-1), ListNode(-1)
        l1, l2 = self.resverse(head1), self.resverse(head2)
        dummy = ListNode(0)
        tmp = dummy
        t = 0
        while l1 != None or l2 != None:
            if l1 != None:
                a = l1.val
            else:
                a = 0
            if l2 != None:
                b = l2.val
            else:
                b = 0
            t = a + b + t
            tmp.next = ListNode(t % 10)
            t = t // 10
            tmp = tmp.next
            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        if t > 0: tmp.next = ListNode(t)
        return self.resverse(dummy.next)