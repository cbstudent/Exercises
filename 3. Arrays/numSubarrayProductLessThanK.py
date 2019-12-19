class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        
        # Approach: Dynamic sliding window
        # O(n) time and O(1) space
        
        if k == 0:
            return 0
        
        currProduct = 1
        countArrs = 0
        start = 0
        
        for end, i in enumerate(nums):
            currProduct *= i
            while currProduct >= k and start < len(nums):
                currProduct //= nums[start]
                start += 1
            countArrs += end - start + 1
            
        if countArrs < 0:
            return 0
        
        return countArrs
            
