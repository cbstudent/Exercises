class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        outdegrees = [0] * numCourses
        indegrees = [[] for _ in range(numCourses)]
        
        for p in prerequisites:
            outdegrees[p[0]] += 1
            indegrees[p[1]].append(p[0])
        dq = []
        for i in range(numCourses):
            if outdegrees[i] == 0:
                dq.append(i)
                
        visited = set()
        
        while dq:
            curr = dq.pop(0)
            visited.add(curr)
            for i in indegrees[curr]:
                outdegrees[i] -= 1
                if outdegrees[i] == 0:
                    dq.append(i)
        return len(visited) == numCourses
