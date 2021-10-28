def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]



nums = [7,8,1,2,3,4,5,6]
print(findMin(nums))
