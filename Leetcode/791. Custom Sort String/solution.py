class Solution:
    def customSortString(self, order: str, s: str) -> str:
      
      mem = {}
      
      for i in range(len(s)):
        if s[i] not in mem: 
          if s[i] not in order: 
            mem[s[i]] = [float('inf'), 1]
          else: 
            mem[s[i]] = [order.index(s[i]), 1] 
        else:
          temp = mem[s[i]]
          temp[1] += 1
          mem[s[i]] = temp 
        
      priorities = sorted(mem.items(), key=lambda x: x[1]) 
      
      new = ''
      
      for o in priorities:
        times = o[0] * o[1][1]
        new += times  
      
      return new
        
      
      
        
