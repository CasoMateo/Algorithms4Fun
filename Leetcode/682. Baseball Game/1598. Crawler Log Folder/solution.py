class Solution:
    def minOperations(self, logs: List[str]) -> int:
  
      cur = 0 
          
      for i in range(len(logs)):
        if logs[i] == '../':
          if cur > 0:
            cur -= 1
        
        elif logs[i] != './':
          cur += 1 
      
      return cur
