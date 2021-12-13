class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
      
      mem = {}
      
      for num in arr: 
        cur = bin(num).count('1')
        if cur in mem: 
          mem[cur].append(num)
          
        else:
          mem[cur] = [num]
        
      mem = dict(sorted(mem.items(), key = lambda x: x[0]))
      increasing = []
      
      for order in mem: 
        mem[order] = sorted(mem[order])
        for tok in mem[order]:
          increasing.extend([tok])
      
      return increasing
      
                                                
