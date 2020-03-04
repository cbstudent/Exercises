import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        # Euclidian distance:
        # sqrt(p1² + p2²)

        arr = []
        
        for i in range(K):
            distance = self.getDistance(points[i])
            heapq.heappush(arr, (-distance, points[i]))
        
        for point in points[K:]:
            distance = self.getDistance(point)
            if -distance > arr[0][0]:
                heapq.heappop(arr)
                heapq.heappush(arr, (-distance, point))
        
        res = []
    
        while arr:
            res.append(heapq.heappop(arr)[1])
        
        return res

    def getDistance(self, p):
        return math.sqrt(p[0] ** 2 + p[1] ** 2)
