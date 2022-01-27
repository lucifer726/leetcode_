class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(i, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1] == m


s = "abc"
t = "ahbgdc"
a = Solution()
print(a.isSubsequence(s, t))
