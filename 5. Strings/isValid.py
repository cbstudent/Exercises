class Solution:
    def isValid(self, S: str) -> bool:
        while "abc" in S:
            S = S.replace("abc", "")
            
        if len(S) > 0:
            return False
        else: 
            return True
