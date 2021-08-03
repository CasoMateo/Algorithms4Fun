class Solution:
    def mySqrt(self, x: int) -> int:
      
      if x <= 1: 
        return x
      
      sqrt = 0
      lo = 1
      hi = x // 2
      
      while lo <= hi:
        
        cur = (lo + hi) // 2
        
        if cur ** 2 > x: 
          hi = cur - 1
        else: 
          if x - (cur ** 2) < (x - sqrt): 
            sqrt = cur  
          lo = cur + 1
      
      return sqrt
