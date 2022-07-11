# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        # 该子树没找到，返回-1
        if not root:
            return -1
        # 该节点是其中某一个节点
        if root.val == o1 or root.val == o2:
            return root.val
        # 左子树寻找公共祖先
        left = self.lowestCommonAncestor(root.left, o1, o2)
        # 右子树寻找公共祖先
        right = self.lowestCommonAncestor(root.right, o1, o2)
        # 左子树为没找到，则在右子树中
        if left == -1:
            return right
        # 右子树没找到，则在左子树中
        if right == -1:
            return left
        # 否则是当前节点
        return root.val
