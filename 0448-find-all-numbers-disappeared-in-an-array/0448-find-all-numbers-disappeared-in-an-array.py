class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[]
        n=len(nums)
        nums=set(nums)
        for i in range(1, n+1):
            if i not in nums:
                x.append(i)
        return x