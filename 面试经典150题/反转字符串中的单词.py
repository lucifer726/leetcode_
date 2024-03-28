class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = s.strip().split()

        return " ".join(s1[::-1])

a = Solution()
s = "a good   example"
print(a.reverseWords(s))
