from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        x=[]
        for i in permutations(nums):
            x.append(i)
        return ([list(i) for i in sorted(set(x))])