class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global result
        result, track = [], []
        self.backtrack(nums, track)
        return result

    def backtrack(self, nums,  track):
        if len(track) == len(nums):
            result.append(track[:])
            return
        for i in range(0, len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track)
            track.pop()


nums = [1, 2, 3]
a = Solution()
print(a.permute(nums))
