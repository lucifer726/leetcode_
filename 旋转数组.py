# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution:
    def rotate(self, nums, k: int):
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums


a = Solution()
nums = [-1, 0, 3, 5, 9, 12]
print(a.rotate(nums, 3))
