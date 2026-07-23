class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=[]
        for i in nums:
            if x.count(i)<2:
                x.append(i)
        nums[:len(x)] = x
        return len(x)