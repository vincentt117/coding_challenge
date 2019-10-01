# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aster_stack = []
        for aster in asteroids:
            to_add = aster
            while aster_stack and to_add and aster_stack[-1] > 0 and to_add < 0:
                stack_top = aster_stack.pop()
                if stack_top > abs(aster):
                    to_add = stack_top
                elif stack_top < abs(aster):
                    to_add = aster
                else:
                    to_add = None
            if to_add:
                aster_stack.append(to_add)
        return aster_stack
                    
        