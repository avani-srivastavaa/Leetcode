class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        x=[]
        st=list(map(int, startTime.split(':')))
        et=list(map(int, endTime.split(':')))
        for i in range(0,len(et)):
            for j in range(0,len(st)):
                if i==j:
                    x.append(et[i]-st[j])
        return (x[0]*3600+x[1]*60+x[2])