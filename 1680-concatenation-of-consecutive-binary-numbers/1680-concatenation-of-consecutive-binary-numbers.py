class Solution:
    def concatenatedBinary(self, n: int) -> int:
        x=[]
        i=1
        while i<=n:
            x.append(bin(i)[2:])
            i+=1
        y=''.join(x)
        z=int(y, 2)
        return z % (10**9 + 7)