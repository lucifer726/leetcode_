class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack, res_dict = [], dict()
        for i in nums2:
            while stack and i > stack[-1]:
                small = stack.pop()
                res_dict[small] = i
            stack.append(i)
        return [res_dict[num] if num in res_dict else -1 for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
a = Solution()
print(a.nextGreaterElement(nums1, nums2))
