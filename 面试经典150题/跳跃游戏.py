class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 1:
            return True
        dp = [0 for _ in range(l-1)]
        dp[0] = nums[0]
        for i in range(1,l-1):
            dp[i] = max(dp[i-1] - 1, nums[i])
        if 0 in dp:
            return False
        else:
            return True

a = Solution()
nums = [2,3,1,1,4]
print(a.canJump(nums))