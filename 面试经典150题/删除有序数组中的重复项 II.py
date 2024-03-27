class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, f = 0, 1
        e = 0
        while len(nums) > f:
            if nums[s] == nums[f] and e == 0:
                e += 1
                f += 1
                s += 1
                nums[s] = nums[s-1]
            elif nums[s] == nums[f] and e != 0:
                f += 1
            else:
                s += 1
                nums[s], nums[f] = nums[f], nums[s]
                f += 1
                e = 0
        nums = nums[:s+1]
        return len(nums)

a = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(a.removeDuplicates(nums))
