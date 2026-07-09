from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        for i,j in Counter(nums).items():
            if j>n/2:
                return i
        return