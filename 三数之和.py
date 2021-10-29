def threeSum(nums):
    ans = list()
    if len(nums) < 3:
        return ans
    nums.sort()
    a = 0
    if nums[a] > 0:
        return ans
    for a in range(len(nums)):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        b = a + 1
        c = len(nums) - 1
        while b < c:
            sums = nums[a] + nums[b] + nums[c]
            if sums == 0:
                ans.append([nums[a], nums[b], nums[c]])
                while b < c and nums[b] == nums[b + 1]: b += 1
                while b < c and nums[c] == nums[c - 1]: c -= 1
                b += 1
                c -= 1
            elif sums < 0:
                b += 1
            else:
                c -= 1
        a += 1
    return ans


nums = [0, 0, 0, 0]
print(threeSum(nums))
