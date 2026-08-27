class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        ans = float('inf')

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []

            positions[num].append(i)

            if len(positions[num]) >= 3:
                p = positions[num]
                distance = 2 * (p[-1] - p[-3])
                ans = min(ans, distance)

        return -1 if ans == float('inf') else ans