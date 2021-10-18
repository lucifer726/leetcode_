def reverseString(s):
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
