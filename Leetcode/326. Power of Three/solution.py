class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      
      lo = 1 
      hi = 31
      
      while lo <= hi: 
        cur = (lo + hi) // 2 
        
        if 3 ** cur < n: 
          lo = cur + 1
        
        elif 3 ** cur > n: 
          hi = cur - 1
        
        else: 
          return True
      
      return True if n == 1 else False
