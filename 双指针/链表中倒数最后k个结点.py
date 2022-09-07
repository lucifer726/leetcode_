class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        if not pHead:
            return None
        fast = pHead
        slow = pHead
        while fast and k > 0:
            fast = fast.next
            k -= 1
        if k > 0:
            return None
        while fast:
            slow = slow.next
            fast = fast.next
        return slow