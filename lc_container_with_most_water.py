# https://leetcode.com/problems/container-with-most-water/description/
def maxArea(height):
    maxVol = 0
    l, r = 0, len(height) - 1
    while(l<r):
        maxVol = max(maxVol, min(height[l], height[r]) * (r - l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return maxVol

# Got optimized solution from prob. solution.

