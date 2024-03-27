class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s, f = 0, 1
        b = 0
        while f < len(prices):
            if prices[s] < prices[f]:
                b += prices[f] - prices[s]
                f += 1
                s += 1
            else:
                f += 1
                s += 1
        return b


a = Solution()
p = [7,6,4,3,1]
print(a.maxProfit(p))
