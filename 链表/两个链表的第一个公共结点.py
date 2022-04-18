class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        a = pHead1
        b = pHead2
        while a != b:
            a = a.next if a else pHead2
            b = b.next if b else pHead1
        return a