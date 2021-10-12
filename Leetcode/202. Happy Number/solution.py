class Solution:
    def isHappy(self, n: int) -> bool:
      
      if n == 1: 
        return True 
      
      cur = n
      mem = set()
      
      while int(cur) != 1: 
        ac = 0 
        
        for digit in str(cur): 
          ac += int(digit) ** 2 
        
        cur = ac 
        
        if cur == 1: 
          return True 
        
        if cur in mem: 
          return False
      
        mem.add(cur)
