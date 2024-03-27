class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        lens_1 = len(nums1)
        p = lens_1
        while p > 0 and n > 0:
            if m == 0:
                nums1[:n] = nums2[:n]
                return nums1
            if nums2[n -1] >= nums1[m - 1]:
                nums1[lens_1 - 1] = nums2[n - 1]
                lens_1 = lens_1 - 1
                n = n - 1
            else:
                nums1[lens_1 - 1] = nums1[m - 1]
                lens_1 = lens_1 - 1
                m = m - 1
        return nums1

a = Solution()
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
print(a.merge(nums1,m,nums2,n))