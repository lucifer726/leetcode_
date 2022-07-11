class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # 空树找不到公共祖先
        if not root:
            return -1
        # pq在该节点两边说明这就是最近公共祖先
        if (p >= root.val >= q) or (p <= root.val <= q):
            return root.val
        # pq都在该节点的左边
        elif p <= root.val and q <= root.val:
            # 进入左子树
            return self.lowestCommonAncestor(root.left, p, q)
            # pq都在该节点的右边
        else:
            # 进入右子树
            return self.lowestCommonAncestor(root.right, p, q)
