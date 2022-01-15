class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        import numpy as np
        envelopes= np.array(envelopes)
        idex = np.lexsort([-1 * envelopes[:, 1], envelopes[:, 0]])
        sorted_data = envelopes[idex, :]
        height = [0] * n
        for i in range(n):
            height[i] = sorted_data[i][1]

        return self.lengthOfLIS(height)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = [0] * len(nums)
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]
            left = 0
            right = piles
            while left < right:
                mid = left + (right - left) // 2
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


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
a = Solution()
print(a.maxEnvelopes(envelopes))
