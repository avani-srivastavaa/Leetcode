class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        product=1
        i=n
        while i>0:
            i1=i%10
            sum+=i1
            product*=i1
            i=i//10
        return n%(sum+product)==0