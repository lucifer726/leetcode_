class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        global res
        res = []
        self.sort(arr, len(arr))
        return res

    def sort(self, arr, n):
        if n == 1: return
        maxVal = 0
        maxIndex = 0
        for i in range(n):
            if arr[i] > maxVal:
                maxIndex = i
                maxVal = arr[i]
        self.reverse(arr, 0, maxIndex)
        res.append(maxIndex + 1)
        self.reverse(arr, 0, n - 1)
        res.append(n)
        self.sort(arr, n - 1)

    def reverse(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1


arr = [3, 2, 4, 1]
a = Solution()
print(a.pancakeSort(arr))
