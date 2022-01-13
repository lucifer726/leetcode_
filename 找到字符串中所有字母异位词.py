class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for c in p: need[c] += 1
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return res


s = "cbaebabacd"
p = "abc"
a = Solution()
print(a.findAnagrams(s, p))
