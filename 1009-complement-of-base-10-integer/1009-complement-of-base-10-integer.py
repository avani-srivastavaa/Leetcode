class Solution:
    def bitwiseComplement(self, n: int) -> int:
        complement=''
        for bit in bin(n)[2:]:
            if bit=='0':
                complement+='1'
            else:
                complement+='0'
        return (int(complement,2))
