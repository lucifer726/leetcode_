class Solution(object):


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return nums[0]

        def robRange(nums, start, end):
            n = len(nums)
            dp_i_1, dp_i_2, dp = 0, 0, 0
            for i in range(start, end):
                dp_i = max(dp_i_1, nums[i] + dp_i_2)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i

        return max(robRange(nums, 0, n - 1), robRange(nums, 1, n))


a = Solution()
nums = [1,2,3]
print(a.rob(nums))
