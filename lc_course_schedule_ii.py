# https://leetcode.com/problems/course-schedule-ii/
# Optimal

import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.order = []
        self.seen = set()
        self.course_preq = collections.defaultdict(list)
        
        for pre in prerequisites:
            self.course_preq[pre[0]].append(pre[1])
            
        for i in range(numCourses):
            if i in self.course_preq:
                self.path = set()
                self.path.add(i)
                if not self.top_search(self.course_preq[i]): 
                    return []
                del self.course_preq[i]
            if not i in self.seen:
                self.order.append(i)
                self.seen.add(i)
        return self.order
        
    def top_search(self, collection):
        for course in collection:
            if course in self.path:
                return False
            if not course in self.seen:
                self.path.add(course)
                if course in self.course_preq: 
                    if not self.top_search(self.course_preq[course]):
                        return False
                self.path.remove(course)
                self.order.append(course)
                self.seen.add(course)
        return True
                
            
# [1, 0] means 0 -> 1
# take 0 then 1
            
        
            