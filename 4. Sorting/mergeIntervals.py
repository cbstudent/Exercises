class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the input array: O(n log n)
        intervals.sort()
        
        i = 0
        
        # Go through the items and look ahead at the next item
        while i < len(intervals)-1: # O(n)
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max([intervals[i][1], intervals[i+1][1]])
                del intervals[i+1]
            else:
                i += 1
                
        return intervals
