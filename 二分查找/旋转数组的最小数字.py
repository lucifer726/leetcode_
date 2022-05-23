class Solution:
    def minNumberInRotateArray(self , rotateArray):
        l, r = 0, len(rotateArray)-1
        while l < r:
            mid = (r - l) // 2 + l
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            elif rotateArray[mid] == rotateArray[r]:
                r -= 1
            else:
                r = mid
        return rotateArray[l]

a = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(a.minNumberInRotateArray(nums))