class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur, nxt = 1, 1
        for _ in range(n):
            cur, nxt = nxt, cur + nxt
        return cur % 1000000007

n = 7
a = Solution()
print(a.numWays(n))