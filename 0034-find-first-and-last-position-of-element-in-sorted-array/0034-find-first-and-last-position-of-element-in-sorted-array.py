class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=[]
        y=[-1,-1]
        flag=0
        for i in range(0,len(nums)):
            if nums[i]==target:
                x.append(i)
                flag+=1
            i+=1
        if flag==0:
            return y
        if flag==1:
            return x*2
        if flag>=3:
            return x[0], x[-1]
        return x