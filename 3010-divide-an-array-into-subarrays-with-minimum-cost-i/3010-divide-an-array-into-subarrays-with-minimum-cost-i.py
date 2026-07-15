from heapq import nsmallest
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a, b = nsmallest(2, nums[1:])
        return nums[0] + a + b