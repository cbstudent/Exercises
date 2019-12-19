class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Keep track of the longest substring we've seen (so far)
        maxLen = 0 
        
        # Keep track of how often a character appears (max 1 to fulfil the condition) in a dict
        charCount = {}
        
        end = 0
        start = 0
        
        while start < len(s) and end < len(s):
            if s[end] in charCount:
                del(charCount[s[start]])                  
                start += 1
            else:
                charCount[s[end]] = 1
                maxLen = max(maxLen, end - start + 1)
                end += 1
            
        
        return maxLen
        
        
