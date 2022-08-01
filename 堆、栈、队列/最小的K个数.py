class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # write code here
        res = []
        if len(input) >= k and k != 0:
            import heapq
            # 小根堆，每次输入要乘-1
            pq = []
            for i in range(k):
                # 构建一个k个大小的堆
                heapq.heappush(pq, (-1 * input[i]))
            for i in range(k, len(input)):
                # 较小元素入堆
                if (-1 * pq[0]) > input[i]:
                    heapq.heapreplace(pq, (-1 * input[i]))
            # 堆中元素取出入数组
            for i in range(k):
                res.append(-1 * pq[0])
                heapq.heappop(pq)
        return res