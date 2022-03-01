class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans, stack = [-1]*len(nums), []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]
            stack.append(nums[i])
        return ans

nums = [2,1,2,4,3]
a = Solution()
print(a.nextGreaterElements(nums))
