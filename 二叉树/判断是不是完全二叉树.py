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
# @return bool布尔型
#
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # write code here
        already_finish = False
        queue = [root]
        for node in queue:
            if node.left:
                if already_finish:
                    return False
                queue.append(node.left)
            else:
                already_finish = True
            if node.right:
                if already_finish:
                    return False
                queue.append(node.right)
            else:
                already_finish = True

        return True
