class Solution:
    def customSortString(self, order: str, s: str) -> str:
      
      mem = {}
      
      for i in range(len(s)):
        if s[i] in mem: 
          mem[s[i]] += 1 
        else: 
          mem[s[i]] = 1 
          
      permutation = ''
      for j in range(len(order)):
        if order[j] in mem: 
          permutation += order[j] * mem[order[j]] 
        
      for freq in mem: 
        if freq not in order: 
          permutation += freq * mem[freq]
      
      return permutation
