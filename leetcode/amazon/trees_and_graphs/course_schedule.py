"""
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2983/

Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is
             possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take
             course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not
adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    muy interesante
    detectar ciclos en grafo dirigido
    """

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        courses = set(range(numCourses))
        d = defaultdict(list)
        for course, requisite in prerequisites:
            d[course].append(requisite)
        while courses:
            course = courses.pop()
            stack = [course]
            s = {course}
            while stack:
                if d[stack[-1]]:
                    requisite = d[stack[-1]].pop()
                    if requisite in s:
                        return False
                    stack.append(requisite)
                    s.add(requisite)
                    courses.difference_update({requisite})
                else:
                    s.difference_update({stack.pop()})
        return True
