class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]


prices = [7, 1, 5, 3, 6, 4]
a = Solution()
print(a.maxProfit(prices))
