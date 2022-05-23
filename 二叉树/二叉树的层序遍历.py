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
# @return int整型二维数组
#
class Solution:
    def levelOrder(self, root: TreeNode):
        # write code here
        if not root: return []
        # 跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            # 存储当前层的孩子节点列表
            ll = []
            # 对当前层的每个节点遍历
            for node in queue:
                # 如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                # 如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            # 后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res
