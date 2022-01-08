def fun(nums, target):
    Hashtable = dict()
    ans = []
    for i, num in enumerate(nums):
        Hashtable[num] = i
    for i, num in enumerate(nums):
        j = Hashtable.get(target - num)
        if j is not None and i != j:
            ans.append([nums[i], nums[j]])
    n = len(ans)//2
    return ans[:n]


nums = [1, 3, 4, 5, 8]
print(fun(nums, 9))
