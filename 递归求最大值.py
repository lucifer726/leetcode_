def process(arr, L, R):
    """
    :param arr: 数组
    :param L: 左端点
    :param R: 右端点
    :return: 最大值
    """
    if L == R:
        return arr[L]
    mid = L + ((R - L) >> 1)  # 右移一位，比除二运算快
    left = process(arr, L, mid)
    right = process(arr, mid + 1, R)
    return max(left, right)


a = [3, 2, 5, 7, 6, 4]
print(process(a, 0, len(a) - 1))
