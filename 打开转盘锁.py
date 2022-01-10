'''
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

'''

class Solution:
    def openLock(self, deadends, target: str) -> int:
        # 记录需要跳过的死亡密码
        deads = set(deadends)
        # 记录已经穷举过的密码，防止走回头路
        visited = set()
        q = list()
        # 从起点开始启动广度优先搜索
        step = 0
        q.append("0000")
        visited.add("0000")

        while q:
            # 将当前队列中的所有节点向周围扩展
            for i in range(len(q)):
                cur = q.pop(0)

                # 判断密码是否合法，是否达到终点
                if cur in deads: continue
                if cur == target: return step

                # 将一个节点的未遍历相邻节点加入队列
                for j in range(4):
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            # 在这里增加步数
            step += 1
        # 如果穷举完都没找到，返回-1
        return -1

    def plusOne(self, s: str, i: int) -> str:
        """将字符串s的第i个元素向上拨动一位，并返回拨动后的字符串"""
        s_list = list(s)
        if s_list[i] == '9':
            s_list[i] = '0'
        else:
            s_list[i] = str(int(s_list[i]) + 1)
        return "".join(s_list)

    def minusOne(self, s: str, i: int) -> str:
        """将字符串s的第i个元素向下拨动一位，并返回拨动后的字符串"""
        s_list = list(s)
        if s_list[i] == '0':
            s_list[i] = '9'
        else:
            s_list[i] = str(int(s_list[i]) - 1)
        return "".join(s_list)

