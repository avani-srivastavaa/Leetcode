from itertools import combinations
class Solution:
    def largestTriangleArea(self, points):
        def area(a, b, c):
            return abs(
                a[0]*(b[1]-c[1]) +
                b[0]*(c[1]-a[1]) +
                c[0]*(a[1]-b[1])
            ) / 2
        return max(area(a, b, c) for a, b, c in combinations(points, 3))