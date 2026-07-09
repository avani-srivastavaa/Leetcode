class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        l=list(map(int, str(n)))
        digitSum=sum(l)
        squareSum=0
        for i in l:
            squareSum=squareSum+(i*i)
        if squareSum-digitSum >= 50:
            return True
        return False