class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n={}
        x=[]
        for i in strs:
            key = "".join(sorted(i.lower()))
            if key in n:
                n[key].append(i)
            else:
                n[key] = [i]
        return list(n.values())