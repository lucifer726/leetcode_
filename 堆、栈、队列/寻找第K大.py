class Solution:
    def findKth(self , a: List[int], n: int, K: int) -> int:
        # write code here
        return sorted(a, reverse= True)[K-1]