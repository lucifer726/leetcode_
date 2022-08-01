class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        res = []
        # 窗口大于数组长度的时候，返回空
        if size <= len(num) and size != 0:
            from collections import deque
            # 双向队列
            dq = deque()
            for i in range(size):
                while dq and num[i] >= num[dq[-1]]:
                    dq.pop()
                dq.append(i)
            res.append(num[dq[0]])
            for i in range(size, len(num)):
                while dq and dq[0] <= i - size:
                    dq.popleft()
                while dq and num[i] >= num[dq[-1]]:
                    dq.pop()
                dq.append(i)
                res.append(num[dq[0]])
        return res


