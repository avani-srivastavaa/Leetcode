from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        for i,v in Counter(nums).items():
            if v==1:
                sum+=i
        return sum