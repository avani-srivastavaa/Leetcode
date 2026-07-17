from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t=list(t)
        s=list(s)
        for i in s:
            if i in t:
                t.remove(i)
        return ''.join(t)