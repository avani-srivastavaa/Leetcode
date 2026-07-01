from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1.split()+s2.split()
        print(s)
        x=[]
        for i,v in Counter(s).items():
            if v==1:
                x.append(i)
        return x