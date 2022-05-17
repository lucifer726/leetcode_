def search(nums, target):
    l, r = 0, len(nums)
    while l <= r:
        mid = (r - l) // 2 + l
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))
