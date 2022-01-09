
res = []

# 主函数，输入一组不重复的数字，返回它们的全排列
def permute(nums):
    # 记录“路径”
    track = []
    backtrack(nums, track)
    return res


# 路径：记录在track中
# 选择列表：nums中不存在于track的那些元素
# 结束条件：nums中的元素全都在track中出现
def backtrack(nums, track):
    # 触发结束条件
    if len(track) == len(nums):
        res.append(track.copy())
        print('当前res是: ' + str(res))
        return res

    for i in nums:
        # 排除不合法的选择
        if i in track: continue
        # 做选择
        track.append(i)
        # 进入下一层决策树
        backtrack(nums, track)
        # 取消选择
        track.pop()


nums = [1, 2, 3]
print(permute(nums))

