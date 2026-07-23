from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=[]
        for i,v in Counter(nums).items():
            if v==1:
                x.append(i)
        return x