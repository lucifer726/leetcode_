class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:
                res.append(paths)
                return

            dfs(paths + '(', left + 1, right)
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res


n = 3
a = Solution()
print(a.generateParenthesis(n))
