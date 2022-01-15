class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = [0]*len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]
            left = 0
            right = piles
            while left < right:
                mid = left + (right - left)//2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            if left == piles:
                piles += 1
            top[left] = poker
        return piles



nums = [10, 9, 2, 5, 3, 7, 101, 18]
a = Solution()
print(a.lengthOfLIS(nums))
