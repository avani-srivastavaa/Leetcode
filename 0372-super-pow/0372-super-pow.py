class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        exponent = int("".join(map(str, b)))
        return pow(a, exponent, 1337)