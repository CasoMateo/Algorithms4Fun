class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
      
      mem = {}
      
      for i in range(len(mat)):
        cur = 0 
        
        for j in range(len(mat[0])):
          if mat[i][j] == 1:
            cur += 1
            
        mem[i] = cur
    
      priorities = dict(sorted(mem.items(), key = lambda item: item[1]))
      indices = []
      
      for strength in priorities:
        k -= 1 
        
        if k < 0: 
          break
        
        indices.append(strength)
      
      return indices
