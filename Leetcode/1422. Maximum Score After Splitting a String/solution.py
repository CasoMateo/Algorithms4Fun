class Solution:
    def maxScore(self, s: str) -> int:
      
      mem0 = {}
      cur = 0
      
      for i in range(len(s)):
        if s[i] == '0':
          cur += 1 
        
        mem0[i] = cur 
      
      mem1 = {}
      cur = 0 
      for j in range(len(s)):
        if s[len(s) - j - 1] == '1':
          cur += 1 
        
        mem1[len(s) - j - 1] = cur
     
      score = 0
      for k in range(len(s) - 1):
        score = max(score, mem0[k] + mem1[k + 1])
        
      return score
  
