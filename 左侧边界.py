def left_bound(nums, target):
    if len(nums) == 0: return -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    if left > len(nums) - 1 or nums[left] != target:
        return -1
    return left


nums = [1, 1, 2, 2, 3, 3, 4, 4]
target = 2
print(left_bound(nums, target))
