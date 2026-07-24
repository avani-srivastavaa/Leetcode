class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        d1 = []
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                d1.append(prices[i] - prices[i - 1])
        return sum(d1)