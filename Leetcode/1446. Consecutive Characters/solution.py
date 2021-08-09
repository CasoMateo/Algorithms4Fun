class Solution:
    def maxPower(self, s: str) -> int:
      largest = cur = 1
      
      for i in range(1, len(s)):
        if s[i - 1] == s[i]:
          cur += 1 
        else: 
          largest = max(largest, cur)
          cur = 1 
      
      largest = max(largest, cur)
      
      return largest
        
