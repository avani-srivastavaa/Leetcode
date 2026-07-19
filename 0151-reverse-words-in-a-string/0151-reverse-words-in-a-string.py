class Solution:
    def reverseWords(self, s: str) -> str:
        x=[]
        for word in s.split():
            x.append(word)
        x.reverse()
        return " ".join(x)