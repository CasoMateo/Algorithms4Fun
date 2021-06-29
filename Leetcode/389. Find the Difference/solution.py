class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      mem = {}
      
      for char in s: 
        mem[char] = mem.get(char, 0) + 1
        
      for pos in t: 
        if pos not in mem: 
          return pos
        mem[pos] -= 1
        
      for oc in mem:
        if mem[oc] != 0: 
          return oc
