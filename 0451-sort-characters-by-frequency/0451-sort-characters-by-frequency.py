from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s=list(s)
        p=[]
        c=Counter(s)
        sorted_dict = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
        for i,v in sorted_dict.items():
            for j in range(v):
                p.append(i)
        return ''.join(p)