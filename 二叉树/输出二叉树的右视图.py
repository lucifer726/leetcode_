# Definition
# for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = []
        queue.append(root)
        while queue:
            ans.append(queue[-1].val)
            for i in range(len(queue)):
                value = queue[0]
                del queue[0]
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
        return ans
