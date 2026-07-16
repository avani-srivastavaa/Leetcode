class Solution:
    def reverseVowels(self, s: str) -> str:
        x=[]
        s=list(s)
        for i in s:
            if i in 'AEIOUaeiou':
                x.append(i)
        x.reverse()
        j=0
        for i in range(len(list(s))):
            if s[i] in 'AEIOUaeiou':
                s[i]=x[j]
                j+=1
        return ''.join(s)