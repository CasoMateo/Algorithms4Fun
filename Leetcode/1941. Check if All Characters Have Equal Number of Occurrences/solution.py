class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
      
      mem = {}
      
      for char in s: 
        mem[char] = mem.get(char, 0) + 1
        
      return len(set(mem.values())) == 1 
        
