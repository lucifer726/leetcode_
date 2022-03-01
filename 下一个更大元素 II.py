class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res, stack = [-1] * n, []
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            res[i % n] = -1 if not stack else stack[-1]
            stack.append(nums[i % n])
        return res


nums = [1, 2, 3, 4, 3]
a = Solution()
print(a.nextGreaterElements(nums))
