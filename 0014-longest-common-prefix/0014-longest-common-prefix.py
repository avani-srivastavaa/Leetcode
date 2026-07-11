class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]
        ans=[]
        for i in strs:
            while not i.startswith(p):
                p = p[:-1]
        ans.append(p if p else "")
        return ''.join(ans)

