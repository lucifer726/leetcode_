class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left, right = 0, len(nums)
        while (left < right):
            mid = (right - left) // 2 + left
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


a = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(a.searchInsert(nums, target))
