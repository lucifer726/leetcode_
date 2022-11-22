class Solution:
    """递归法 更快"""

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxvalue = max(nums)
        index = nums.index(maxvalue)

        root = TreeNode(maxvalue)

        left = nums[:index]
        right = nums[index + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root