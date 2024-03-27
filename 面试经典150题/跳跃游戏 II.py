class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [float("inf") for _ in range(size)]
        dp[0] = 0

        j = 0
        for i in range(1, size):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1

        return dp[size - 1]

a = Solution()
nums = [2, 3, 1, 1, 4]
print(a.jump(nums))