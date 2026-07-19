class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        y=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=x:
                y.append(True)
            else:
                y.append(False)
        return y