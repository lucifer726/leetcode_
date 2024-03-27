class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop(-1)
            else:
                i = i + 1

        return len(nums)

a = Solution()
nums = [3,2,2,3]
val = 3
print(a.removeElement(nums, val))