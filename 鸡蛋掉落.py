class Solution(object):
    def superEggDrop1(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        memo = dict()

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]

            res = n + 1
            for i in range(1, n + 1):
                res = min(res, max(dp(k, n - i), dp(k - 1, i - 1)) + 1)

            memo[(k, n)] = res
            return res

        return dp(k, n)

    def superEggDrop2(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        memo = dict()

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]

            res = n + 1
            lo, hi = 1, n
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(k - 1, mid - 1)
                not_nroken = dp(k, n - mid)
                if broken > not_nroken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_nroken + 1)

            memo[(k, n)] = res
            return res

        return dp(k, n)


k = 3
n = 14
a = Solution()
print(a.superEggDrop1(k, n))
print(a.superEggDrop2(k, n))

