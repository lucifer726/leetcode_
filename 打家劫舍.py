class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_i_1, dp_i_2 = 0, 0
        for i in range(0, n):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i_1


a = Solution()
nums = [2, 1, 7, 9, 3, 1]
print(a.rob(nums))
