class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        groups = []
        for i in range(0, len(s), k):
            groups.append(s[i:i+k])
        return "-".join(groups)[::-1]