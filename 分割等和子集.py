class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        if _sum % 2 != 0: return False
        n = len(nums)
        _sum = _sum // 2
        dp = [False for _ in range(_sum + 1)]
        dp[0] = True
        for i in range(0, n):
            for j in range(_sum,-1,-1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[_sum]


a = Solution()
nums = [1, 5, 11, 5]
print(a.canPartition(nums))
