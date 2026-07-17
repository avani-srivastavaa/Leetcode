class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=[]
        for i,j in zip(word1, word2):
            x.append(i+j)
        x.append(word1[len(word2):])
        x.append(word2[len(word1):])
        return ''.join(x)
