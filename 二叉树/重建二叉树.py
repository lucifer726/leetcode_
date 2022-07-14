class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self, pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        n = len(pre)
        m = len(vin)
        # 每个遍历都不能为0
        if n == 0 or m == 0:
            return None
        # 构建根节点
        root = TreeNode(pre[0])
        for i in range(len(vin)):
            # 找到中序遍历中的前序第一个元素
            if pre[0] == vin[i]:
                # 左子树的前序遍历
                leftpre = pre[1:i + 1]
                # 左子树的中序遍历
                leftvin = vin[:i]
                # 构建左子树
                root.left = self.reConstructBinaryTree(leftpre, leftvin)
                # 右子树的前序遍历
                rightpre = pre[i + 1:]
                # 右子树的中序遍历
                rightvin = vin[i + 1:]
                # 构建右子树
                root.right = self.reConstructBinaryTree(rightpre, rightvin)
                break
        return root
