from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x=[]
        for i,v in Counter(nums).items():
            if v==2:
                x.append(i)
        return x