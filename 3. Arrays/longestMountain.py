class Solution:
    def longestMountain(self, A) -> int:
        
        max_len = 0
        
        for i in range(1, len(A) - 1):
            if A[i-1] < A[i] and A[i] > A[i+1]: # look for peaks
                # At each peak, look to the left and to the right
                left = i-1
                right = i+1
                
                while left > 0 and A[left] > A[left-1]:
                    left -= 1
                
                while right < len(A) - 1 and A[right] > A[right+1]:
                    right += 1
                
                max_len = max(max_len, right - left + 1)
                                
        
        return max_len
