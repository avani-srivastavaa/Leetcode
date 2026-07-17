from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,v in Counter(s).items():
            if v==1:
                return s.index(i)
        return -1
            