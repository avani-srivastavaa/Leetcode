class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        d1=d=0
        for i in range(len(prices)):
            if prices[i]>minn:
                d=prices[i]-minn
                if d>d1:
                    d1=d
            if prices[i]<minn:
                minn=prices[i]
        return d1
