class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]


amount = 5
coins = [1, 2, 5]
a = Solution()
print(a.change(amount, coins))
