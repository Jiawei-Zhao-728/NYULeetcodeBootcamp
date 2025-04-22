from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree array
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # Queue for all nodes with 0 indegree
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []
