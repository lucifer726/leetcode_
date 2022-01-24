class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1]]
        for i in range(1, numRows):
            dp.append([1])
            for j in range(1, i):
                dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])

            dp[i].append(1)
        return dp

numRows = 6
a = Solution()
print(a.generate(numRows))