class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        for word in s.split():
            l.append(word)
        l1=l[::-1]
        res=" ".join(l1)
        return res