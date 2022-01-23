class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        if not s and len(p) == 1: return False

        m = len(s) + 1
        n = len(p) + 1

        dp = [[False for _ in range(n)] for _ in range(m)]

        dp[0][0] = True

        # 确定dp数组的第一行，如果遇到了*,只要判断其对应的前面两个元素的dp值
        # 注意：我们无需判断p里面的第一个值是否为"*"，如果为"*",那肯定匹配不到为Fasle,原数组正好是Fasle，所以直接从2开始判断即可
        for j in range(2, n):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for r in range(1, m):
            i = r - 1  # 对应s中的元素
            for c in range(1, n):
                j = c - 1  # 对应p中的元素
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False

        return dp[m - 1][n - 1]


s = "aab"
p = "c*a*b"
a = Solution()
print(a.isMatch(s, p))
