class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                count += 1
        return min(count, len(s) - count)