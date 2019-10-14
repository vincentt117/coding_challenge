# https://leetcode.com/problems/trapping-rain-water/submissions/

class Solution:
#     def trap(self, height: List[int]) -> int: # Stack
#         water = 0
#         l, r = 0, 0
#         land_stack = []
#         while r < len(height):
#             left = None
#             while land_stack and land_stack[-1][0] <= height[r]:
#                 left = land_stack.pop()
#                 water += (r - left[1] - 1) * (left[0] - left[2])
#                 if land_stack:
#                     land_stack[-1][2] = left[0]
#             if land_stack and left and height[r] > left[0] and land_stack[-1][0] > height[r] and r - land_stack[-1][1] > 1:
#                 water += (r - land_stack[-1][1]- 1) * (height[r] - land_stack[-1][2])
#                 land_stack[-1][2] = height[r]
                
#             land_stack.append([height[r], r, 0])
#             r += 1
                
#         return water
    
    def trap(self, height: List[int]) -> int: # DP
        max_left_right = [[0, 0] for i in range(len(height))]
        max_left = 0
        for i, v in enumerate(height):
            max_left = max(max_left, v)
            max_left_right[i][0] = max_left
        max_right = 0
        for i in range(len(height) - 1, -1, -1):
            max_right = max(max_right, height[i])
            max_left_right[i][1] = max_right
        water = 0
        for i, v in enumerate(max_left_right):
            water += min(v) - height[i]
        return water
            
        
        
        
        
                
        