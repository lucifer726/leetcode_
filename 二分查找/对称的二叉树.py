# 给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True

        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right,
                                                                                           right.left)
        return isMirror(pRoot.left, pRoot.right)
