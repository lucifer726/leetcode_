# 一个数组中，有一种数出现奇数次，其他的数，都出现了偶数次，找到这个奇数次对应的数

def findji(arr):
    sum = 0
    for i in range(len(arr)):
        sum ^= arr[i]
    print(sum)


a = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 5, 6, 7]
findji(a)

# 一个数组中，有两种数出现奇数次，其他的数，都出现了偶数次，找到这两个奇数次对应的数

def findtwoji(arr):
    eor = 0
    for i in range(len(arr)):
        eor ^= arr[i]
    rightone = eor & (~eor + 1)
    for j in range(len(arr)):
        if arr[j]&rightone == 1:
            rightone ^= arr[j]
    print(rightone,rightone^eor)


b = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 5, 6, 7, 8]
findtwoji(b)
