# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
def moveZeroes(nums):
    n = len(nums)
    left, right = 0, 0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums


a = [0, 1, 0, 3, 12]
print(moveZeroes(a))
