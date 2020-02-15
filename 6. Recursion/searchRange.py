class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        pos = [-1, -1]
        
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    pos[0] = mid
                    break
                else:
                    hi = mid - 1

            
        lo = 0 # we could instead start at pos[0] (if post[0] != -1)
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    pos[1] = mid
                    break
                else:
                    lo = mid + 1
        
        return pos
