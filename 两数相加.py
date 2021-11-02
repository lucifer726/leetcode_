class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        add = l1.val + l2.val
        res = ListNode(add % 10)
        res.next = self.addTwoNumbers(l1.next, l2.next)
        if add >= 10:
            res.next = self.addTwoNumbers(res.next, ListNode(1))
        return res


def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')


l1 = [2, 4, 3]
l2 = [5, 6, 4]
s1 = create_linked_list(l1)
s2 = create_linked_list(l2)
solution = Solution()
result = solution.addTwoNumbers(s1, s2)
print('结果：')
print_linked_list(result)
