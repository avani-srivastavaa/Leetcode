class Solution:
    def minimumDistance(self, nums):
        pos = {}
        ans = float('inf')

        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []

            pos[num].append(i)

            if len(pos[num]) >= 3:
                a, b, c = pos[num][-3:]
                ans = min(ans, 2 * (c - a))

        return -1 if ans == float('inf') else ans