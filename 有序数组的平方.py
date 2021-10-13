# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n

        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] * nums[i] < nums[j] * nums[j]:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            else:
                ans[pos] = nums[i] * nums[i]
                i += 1
            pos -= 1
        return ans


a = Solution()
nums = [-1, 0, 3, 5, 9, 12]
print(a.sortedSquares(nums))
