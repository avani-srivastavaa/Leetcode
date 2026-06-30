class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    for l in range(k, len(nums)):
                        if nums[i]+nums[j]+nums[k]==nums[l] and i<j<k<l:
                            ans+=1
        return ans