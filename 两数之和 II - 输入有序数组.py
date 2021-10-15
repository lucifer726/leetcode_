def twoSum(numbers, target):
    n = len(numbers)
    left,right = 0, n-1
    while left < right:
        if numbers[left]+numbers[right]==target:
            return left+1, right+1
        elif numbers[left]+numbers[right]>target:
            right -= 1
        else:
            left += 1





numbers = [1,2,3,4,4,8,10]
a = 8
print(twoSum(numbers, a))
