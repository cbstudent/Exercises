class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if(len(matrix[0])) == 0:
            return False

        
        lo = 0
        hi = len(matrix) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if matrix[mid][0] > target:
                hi = mid - 1
                
            elif  matrix[mid][len(matrix[mid])-1] < target:
                lo = mid + 1
            
            elif matrix[mid][0] <= target and matrix[mid][len(matrix[mid])-1] >= target:
                # The target is contained within this row
                loRow = 0
                hiRow = len(matrix[mid])-1
                
                while loRow <= hiRow:
                    midRow = (loRow + hiRow) // 2
                    
                    if matrix[mid][midRow] > target:
                        hiRow = midRow - 1
                    elif matrix[mid][midRow] < target:
                        loRow = midRow + 1
                    elif matrix[mid][midRow] == target:
                        return True
                return False
        
        return False
                        
