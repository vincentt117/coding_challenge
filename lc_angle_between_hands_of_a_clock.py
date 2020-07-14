# https://leetcode.com/problems/angle-between-hands-of-a-clock/solution/

# Optimal

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr_dg = ((hour % 12) + (minutes / 60)) * 30
        min_dg = minutes * 6
        small = min(hr_dg, min_dg)
        big = max(hr_dg, min_dg)
        res = big - small
        return res if res <= 180 else 360 - res