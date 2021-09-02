class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
      
      mem = {}
      
      for domino in dominoes: 
        cur = str(min(domino[0], domino[1])) + str(max(domino[0], domino[1]))
        
        mem[cur] = mem.get(cur, 0) + 1      
      
      eq = 0 
      
      for freq in mem: 
        if mem[freq] >= 2: 
          eq += mem[freq] * (mem[freq] - 1)
      
      return eq // 2
      
      
      
      

        
