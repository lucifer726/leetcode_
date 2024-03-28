class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 如果行数为1或者字符串长度不足以形成Z字形，则直接返回原字符串
        if numRows == 1 or numRows >= len(s):
            return s

        # 初始化行列表
        rows = [''] * numRows
        # 当前行的位置
        curRow = 0
        # 是否向下移动
        goingDown = False

        for c in s:
            # 将当前字符添加到正确的行
            rows[curRow] += c
            # 如果当前行是第一行或最后一行，改变方向
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            # 根据方向更新当前行
            curRow += 1 if goingDown else -1

        # 将所有行合并为一个字符串并返回
        return ''.join(rows)