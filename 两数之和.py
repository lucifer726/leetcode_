class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        ans = []
        for i, num in enumerate(nums):
            if target - num in hashtable:
                ans.append([hashtable[target - num], i])
            hashtable[nums[i]] = i
        return ans


nums = [1, 3, 4, 5, 8]
a = Solution()
print(a.twoSum(nums, 9))
