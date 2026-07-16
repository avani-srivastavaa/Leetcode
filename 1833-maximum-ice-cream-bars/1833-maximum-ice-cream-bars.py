class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = cost = 0
        costs.sort()
        for i in costs:
            if cost + i <= coins:
                cost += i
                count += 1
            else:
                break
        return count