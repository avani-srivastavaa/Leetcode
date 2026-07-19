class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        s1=[]
        for i in s:
            if i in 'AEIOUaeiou':
                s1.append(i)
        s1.reverse()
        print(s1)
        j=0
        for i in range(len(s)):
            if s[i] in 'AEIOUaeiou':
                s[i]=s1[j]
                j+=1
        return ''.join(s)