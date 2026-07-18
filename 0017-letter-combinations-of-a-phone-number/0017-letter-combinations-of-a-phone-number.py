from itertools import product
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        phone = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        return [
            ''.join(x)
            for x in product(*(phone[d] for d in digits))
        ]