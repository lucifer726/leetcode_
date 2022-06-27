class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        l, r = root, root
        hl, hr = 0, 0
        while l:
            l = l.left
            hl += 1

        while r:
            r = r.right
            hr += 1

        if hl == hr: return pow(2, hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

