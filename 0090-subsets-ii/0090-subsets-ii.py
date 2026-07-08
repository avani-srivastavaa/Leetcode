from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for r in range(len(nums) + 1):
            for x in combinations(nums, r):
                ans.add(x)
        return [list(x) for x in ans]