class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length  # Step 1: 初始化answer数组

        leftProduct = 1
        for i in range(length):  # Step 2: 从左到右计算左侧乘积
            answer[i] = leftProduct
            leftProduct *= nums[i]

        rightProduct = 1
        for i in range(length - 1, -1, -1):  # Step 3: 从右到左计算右侧乘积
            answer[i] *= rightProduct
            rightProduct *= nums[i]

        return answer  # Step 4: 返回结果

a = Solution()
nums = [1,2,3,4]
print(a.productExceptSelf(nums))
