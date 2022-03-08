class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        global result
        if n <= 0 or k <= 0:
            return [[]]
        result, track = [], []
        self.backtrack(n, k, 1, track)
        return result

    def backtrack(self, n, k, start, track):
        if k == len(track):
            result.append(track[:])
        for i in range(start, n+1):
            track.append(i)
            self.backtrack(n, k, i + 1, track)
            track.pop()


n = 4
k = 2
a = Solution()
print(a.combine(n, k))
