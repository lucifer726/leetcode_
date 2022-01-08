# 斐波那契数列
def Fibonacci(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    dp = [0 for _ in range(n)]
    dp[1] = dp[2] = 1
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


print(Fibonacci(20))