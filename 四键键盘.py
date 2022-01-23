# labuladong 第一种解法 第164页
def maxA_1(N):
    from collections import defaultdict
    memo = defaultdict()

    def dp(n, a_num, copy):
        if n <= 0: return a_num
        if (n, a_num, copy) in memo:
            return memo[(n, a_num, copy)]

        memo[(n, a_num, copy)] = max(
            dp(n - 1, a_num + 1, copy),
            dp(n - 1, a_num + copy, copy),
            dp(n - 2, a_num, a_num)
        )
        return memo[(n, a_num, copy)]

    return dp(N, 0, 0)


# labuladong 第二种解法 第166页
def maxA_2(N):
    dp = [0] * (N + 1)
    for i in range(N + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
    return dp[N - 1]


N = 7
print(maxA_1(N))
print(maxA_2(N))
