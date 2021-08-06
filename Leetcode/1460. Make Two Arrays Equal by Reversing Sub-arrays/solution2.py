

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
      
      mem = {}
      
      for num in target: 
        mem[num] = mem.get(num, 0) + 1 
      
      for pos in arr: 
        if pos not in mem: 
          return False 
        else: 
          mem[pos] -= 1 
      
      return len(set(mem.values())) == 1 
