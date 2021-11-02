class Solution:
    def guessNumber(self, n: int) -> int:
      
      lo = 1
      hi = n  
      
      while lo <= hi: 
        
        cur = (lo + hi) // 2 
        
        if guess(cur) == -1:
          hi = cur - 1
      
        elif guess(cur) == 1:
          lo = cur + 1        
        
        else:
          return cur 
