class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            rev = -int(x[:0:-1])
        else:
            rev = int(x[::-1])
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev