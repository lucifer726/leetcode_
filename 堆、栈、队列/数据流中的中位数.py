from heapq import *


class Solution:
    def __init__(self):
        self.A = []  # 小根堆 保存较大一半的数
        self.B = []  # 小根堆 保存较小一半的数

    def Insert(self, num):
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))
        # write code here

    def GetMedian(self):
        # write code here
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
