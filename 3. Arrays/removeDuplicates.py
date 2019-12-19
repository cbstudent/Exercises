class Solution:
    def removeDuplicates(self, nums):
        
        x = 1 # Start at 1 because the first element is always unique
        for i in range(len(nums)-1): # Since we're checking i+1, only go up to the second-to-last element
            if(nums[i] != nums[i+1]):
                nums[x] = nums[i+1]
                x += 1
                
        return x
