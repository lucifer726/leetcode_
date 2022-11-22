from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                if i == 0:
                    result = queue[i].val
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
