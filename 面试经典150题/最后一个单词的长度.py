class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = s.split(" ")
        while len(w[-1]) == 0:
            w.pop()
        return len(w[-1])


a = Solution()
s = "   fly me   to   the moon  "
print(a.lengthOfLastWord(s))