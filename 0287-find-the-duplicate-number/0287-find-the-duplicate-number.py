from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,v in Counter(nums).items():
            if v>=2:
                return i