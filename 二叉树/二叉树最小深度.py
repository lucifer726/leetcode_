class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = list()
        q.append(root)
        # root本身就是一层，将depth初始化为1
        depth = 1

        while q:
            # 将当前队列中的所有节点向四周扩散
            for i in range(len(q)):
                cur = q.pop(0)
                # 判断是否到达终点
                if not cur.left and not cur.right:
                    return depth
                # 将cur的相邻节点加入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 在这里增加步数
            depth += 1

        return depth






