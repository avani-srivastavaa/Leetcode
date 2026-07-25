class Solution:
    def isThree(self, n: int) -> bool:
        x=0
        for i in range(1,n+1):
            if n%i==0:
                x+=1
        return x==3