class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) + 1
        sum = 0
        sub_length = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                sub_length = j - i + 1
                res = min(res, sub_length)
                sum -= nums[i]
                i += 1
        return res if res != len(nums) + 1 else 0
