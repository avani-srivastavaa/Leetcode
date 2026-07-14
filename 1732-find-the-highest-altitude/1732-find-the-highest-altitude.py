class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c=0
        x=[]
        x.append(c)
        for i in gain:
            c=c+i
            x.append(c)
        print(x)
        return max(x)