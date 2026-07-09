class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        d=0
        x=[]
        for i in sorted(nums):
            diff=i-d
            x.append(diff)
            d=i
        if len(x)==1:
            return 0
        if len(x)>1:
            x.remove(x[0])
        return max(x)