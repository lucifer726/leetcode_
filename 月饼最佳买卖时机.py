# 以月饼每天的售价为输入，输出最大利润。例如第二天买，第五天卖，利润为5
def process(arr):
    dp = [0 for x in range(len(arr))]
    result = 0
    if len(arr) <= 2:
        return arr[1] - arr[0] if arr[1] > arr[0] else 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        dp[i] = max(diff + dp[i - 1], 0)
        if dp[i] > result:
            result = dp[i]
    return result


print(process([7, 1, 5, 3, 6, 4]))
