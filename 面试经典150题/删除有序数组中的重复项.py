class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
                j = j + 1
        nums = nums[:i+1]

        return len(nums)

a = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(a.removeDuplicates(nums))