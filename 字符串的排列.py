from collections import defaultdict


def checkInclusion(s1, s2):
    need, window = defaultdict(int), defaultdict(int)
    for c in s1: need[c] += 1

    left, right = 0, 0
    valid = 0
    while right < len(s2):
        c = s2[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while right - left >= len(s1):
            if valid == len(need):
                return True
            d = s2[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
