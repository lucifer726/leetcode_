class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1  # 总油量小于总消耗，无法绕圈

        total, start = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1  # 设定新的起点
                total = 0  # 重置total为0，因为之前的累积是负的，不能作为起点
        return start

a = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(a.canCompleteCircuit(gas, cost))