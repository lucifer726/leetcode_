class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum = 0
        for i in nums: sum += i
        if sum < abs(target) or (sum + target) % 2 == 1: return 0
        return self.subsets(nums, (sum + target) // 2)

    def subsets(self, nums, sum):
        n = len(nums)
        dp = [0 for _ in range(sum + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(sum, -1, -1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] + dp[j - nums[i - 1]]
                else:
                    dp[j] = dp[j]
        return dp[sum]


a = Solution()
nums = [100]
target = -200
print(a.findTargetSumWays(nums, target))
