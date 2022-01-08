def coinChange(coins, amount):
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]



if __name__ == '__main__':
    coins = [1, 5, 8]
    amount = 10
    print(coinChange(coins, amount))





