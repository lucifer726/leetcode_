def searchRange(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (r - l) // 2 + l
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            if nums[l] == target and nums[r] == target:
                return [l, r]
            else:
                if nums[l]<target:
                    l += 1
                if nums[r]>target:
                    r -= 1
    return [-1, -1]


nums = []
target = 6
print(searchRange(nums, target))
