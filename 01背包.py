def bag(n, w, wt, val):
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
    return dp[n][w]


n = 3
w = 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(bag(n, w, wt, val))
