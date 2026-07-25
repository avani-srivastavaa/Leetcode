class Solution:
    def maxProduct(self, n: int) -> int:
        x=list(map(int, str(n)))
        x.sort(reverse=True)
        return x[0]*x[1]