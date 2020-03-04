import heapq

class Solution:
    def findKthSmallest(self, nums, k: int) -> int:
        
        pq = []
        
        # Create a pq of size k
        for i in range(k):
            heapq.heappush(pq, nums[i])    
        
        # Add all other elements
        for i in nums[k:]:
            if i < pq[0]:
                pq.pop()
                heapq.heappush(pq, i)
        
        return pq[k-1]
 
if __name__ == '__main__':
	arr = [1,2,4,5,4,6,7]
	k = 6
	m = Solution()
	print(m.findKthSmallest(arr, k))
