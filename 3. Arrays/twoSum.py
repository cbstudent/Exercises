class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Sort the array (n log n)
        # Retain the original array because we need the indices in the original order
        numsSorted = sorted(nums)
        
        i = 0 # moving from the left to the right
        j = len(nums) - 1 # moving from the right to the left
        
        while i < len(nums) and j > 0:
            if (numsSorted[i] + numsSorted[j] < target):
                i += 1
            elif (numsSorted[i] + numsSorted[j] > target):
                j -= 1
            elif (numsSorted[i] + numsSorted[j] == target):
                return [nums.index(numsSorted[i]), nums.index(numsSorted[j])]
  
    # Fails for the following test case, because .index() returns the *first* occcurence of the object in the list
    # Input
    # [3,3]
    # 6
    # Output
    # [0,0]
    # Expected
    # [0,1]
