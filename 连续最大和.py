def maxsumlist(n, l):
    currsum = l[0]
    maxsum = l[0]
    for i in range(1, n):
        if currsum > 0:
            currsum += l[i]
        else:
            currsum = l[i]
        maxsum = max(currsum, maxsum)
    return maxsum


n = 3
l = [-1, 2, 1]
print(maxsumlist(n, l))
