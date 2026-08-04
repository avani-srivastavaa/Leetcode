class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        count=[]
        for i in range(min(nums), max(nums)):
            if i not in nums:
                count.append(i)
        return count