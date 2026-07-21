from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=[]
        for i, v in Counter(nums).items():
            if v>n/3:
                x.append(i)
        return x