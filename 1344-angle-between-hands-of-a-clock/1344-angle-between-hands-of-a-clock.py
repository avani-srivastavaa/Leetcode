class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle=0.5*abs((60*hour)-(11*minutes))
        return min(angle,360-angle)