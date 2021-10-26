class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
      cur = n + 1
      
      while True: 
        
        mem = {}
        balanced = True
        
        for digit in str(cur):
          mem[digit] = mem.get(digit, 0) + 1
        
        for sep in str(cur):
          if mem[sep] != int(sep):
            balanced = False 
        
        if balanced: 
          return cur 
        
        cur += 1 
