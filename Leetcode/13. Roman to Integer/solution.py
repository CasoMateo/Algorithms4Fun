class Solution:
    def romanToInt(self, s: str) -> int:
        
        mem = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        tot = cur = 0 
        
        for i in range(len(s)):
          
          if mem[s[i]] <= cur:
            tot += mem[s[i]]
          
          else: 
            tot += mem[s[i]] - 2 * cur
          
          cur = mem[s[i]]
    
        return tot
