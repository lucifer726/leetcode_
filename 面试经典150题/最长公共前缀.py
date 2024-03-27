class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # 初始最长公共前缀为第一个字符串
        prefix = strs[0]

        for s in strs[1:]:
            # 检查当前字符串s是否以当前最长公共前缀prefix开始
            # 如果不是，则缩短prefix直到s以prefix开始或者prefix为空
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))