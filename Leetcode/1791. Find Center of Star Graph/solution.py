class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
      mem = {}
      
      for i in range(len(edges[: 2])):
        mem[edges[i][0]] = mem.get(edges[i][0], 0) + 1
        mem[edges[i][1]] = mem.get(edges[i][1], 0) + 1
      
      center = edges[0][0]
      for freq in mem: 
        if mem[freq] > mem[center]:
          center = freq
      
      return center
        
        
