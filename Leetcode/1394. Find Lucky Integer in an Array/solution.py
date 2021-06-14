class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mem = {}
        
        for num in arr: 
          mem[num] = mem.get(num, 0) + 1
      
        res = -1
        for freq in mem:
          if mem[freq] == freq: 
            res = max(res, freq)
        return res
  
            
