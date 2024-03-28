class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 特殊情况处理
        if not needle:
            return 0  # needle为空字符串时，按照题目要求返回0

        len_haystack = len(haystack)
        len_needle = len(needle)

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i + len_needle] == needle:
                return i  # 找到匹配，返回起始索引
        return -1  # 未找到匹配，返回-1

a = Solution()
haystack = "sadbutsad"
needle = "sad"
print(a.strStr(haystack, needle))