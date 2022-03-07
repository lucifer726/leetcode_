class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global result
        result, track = [], []
        self.backtrack(nums, 0, track)
        return result

    def backtrack(self, nums, start, track):
        result.append(track[:])
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()


nums = [1, 2, 3]
a = Solution()
print(a.subsets(nums))
