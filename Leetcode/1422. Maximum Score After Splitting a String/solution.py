
class Solution:
    def maxScore(self, s: str) -> int:
      
      mem = {}
      cur = 0 
      for j in range(len(s)):
        if s[len(s) - j - 1] == '1':
          cur += 1 
        
        mem[len(s) - j - 1] = cur
     
      score = cur = 0
      
      for k in range(len(s) - 1):
        if s[k] == '0':
          cur += 1
          
        score = max(score, cur + mem[k + 1])
        
      return score
      
  
