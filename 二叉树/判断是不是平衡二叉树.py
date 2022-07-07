class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        def recur(root):
            if root is None:
                return 0
            # 判断左子树是否平衡
            left = recur(root.left)
            if left == -1:
                return -1
            # 判断右子树是否平衡
            right = recur(root.right)
            if right == -1:
                return -1
            # 判断左右子树高度差是否超过1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(pRoot) != -1
