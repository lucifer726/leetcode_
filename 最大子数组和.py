class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)


a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(a.maxSubArray(nums))
