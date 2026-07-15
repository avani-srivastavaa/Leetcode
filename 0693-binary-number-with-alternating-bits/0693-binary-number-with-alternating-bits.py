class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)[2:]
        b=list(b)
        for i in range(0,len(b)-1):
            if b[i]==b[i+1]:
                return False
        return True
