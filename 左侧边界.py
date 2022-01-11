def left_bound(nums, target):
    if len(nums) == 0: return -1
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    return left


nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4]
target = 2
print(left_bound(nums, target))
