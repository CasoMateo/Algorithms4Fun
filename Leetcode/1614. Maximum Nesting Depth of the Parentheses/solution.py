class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack += 1 
                depth = max(depth, stack)
                
            
            elif s[i] == ')':
                stack -= 1 
            
        return depth
        
                
