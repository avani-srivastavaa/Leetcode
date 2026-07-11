class Solution:
    def processStr(self, s: str) -> str:
        st=list(s)
        t=[]
        for i in st:
            if i.isalpha():
                t.append(i)
            elif i=='#':
                t=t+t
            elif i=='%':
                t.reverse()
            elif i=='*':
                if t:
                    t.pop()
        return (''.join(t))