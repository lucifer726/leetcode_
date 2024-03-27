class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums = nums + nums
        return nums[l-k:2*l-k]

a = Solution()
nums = [-1,-100,3,99]
k = 2
print(a.rotate(nums,k))