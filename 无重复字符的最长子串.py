def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    from collections import defaultdict
    window = defaultdict(int)
    left, right = 0, 0
    res = 0
    while right < len(s):
        c = s[right]
        right += 1
        window[c] += 1

        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1

        res = max(res, right - left)

    return res


s = "pwwkew"
print(lengthOfLongestSubstring(s))