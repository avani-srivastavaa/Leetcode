from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i,v in Counter(nums).items():
            if v>=2:
                return True
        return False