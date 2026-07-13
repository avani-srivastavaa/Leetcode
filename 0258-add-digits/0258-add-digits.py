class Solution:
    def addDigits(self, num: int) -> int:
        summ = num
        while len(str(summ)) > 1:
            num = list(str(summ))
            summ = 0
            for i in num:
                summ += int(i)
        return summ