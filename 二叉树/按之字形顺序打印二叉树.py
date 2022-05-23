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
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode):
        if not pRoot:
            return []
        res = []
        stack = [pRoot]
        index = 1
        while stack:
            tmp = []
            for i in range(len(stack)):
                node = stack[0]
                stack = stack[1:]
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if index % 2 == 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            index += 1
        return res