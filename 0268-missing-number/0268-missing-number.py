class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while i <= max(nums)+1:
            if i not in nums:
                return i
            i=i+1