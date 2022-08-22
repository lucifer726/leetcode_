class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            return res
        record = set()
        while True:
            n = cal(n)
            if n == 1:
                return True
            if n in record:
                return False
            record.add(n)