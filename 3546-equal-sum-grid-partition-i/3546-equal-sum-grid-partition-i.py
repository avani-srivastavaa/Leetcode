class Solution:
    def canPartitionGrid(self, grid):
        m = len(grid)
        n = len(grid[0])

        total = sum(map(sum, grid))

        # If total is odd, equal partition is impossible
        if total % 2 != 0:
            return False

        target = total // 2

        # Horizontal cut
        curr = 0

        for i in range(m - 1):   # cut cannot be after last row
            curr += sum(grid[i])

            if curr == target:
                return True

        # Vertical cut
        curr = 0

        for j in range(n - 1):   # cut cannot be after last column
            for i in range(m):
                curr += grid[i][j]

            if curr == target:
                return True

        return False