class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Two-pass solution        
        #red = 0
        #white = 0
        #blue = 0
        #
        #for i in nums:
        #    if i == 0:
        #        red += 1
        #    elif i == 1:
        #        white += 1
        #    elif i == 2:
        #        blue += 1
        #
        #cur = 0
        #for x in range(red):
        #    nums[cur] = 0
        #    cur += 1
        #for x in range(white):
        #    nums[cur] = 1
        #    cur += 1
        #for x in range(blue):
        #    nums[cur] = 2
        #    cur += 1
        
        
        
        # QuickSort solution
        _quickSort(nums, 0, len(nums)-1)
        
def _quickSort(arr, lo, hi):
    
    if lo >= hi:
        return
    
    pivot = partition(arr, lo, hi)
    
    _quickSort(arr, lo, pivot - 1)
    
    _quickSort(arr, pivot + 1, hi)
    
    
def partition(arr, lo, hi):
    pivot = arr[lo]
    swap_index = lo + 1

    for i in range(lo + 1, hi + 1):
        if arr[i] < pivot:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
        
    arr[lo], arr[swap_index - 1] = arr[swap_index - 1], arr[lo]
    
    return swap_index - 1
        
        
        
        
        
