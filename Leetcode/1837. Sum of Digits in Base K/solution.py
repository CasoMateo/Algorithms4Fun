class Solution:
    def sumBase(self, n: int, k: int) -> int:

      digits = 0
 
      while n != 0: 
        if k > n: 
          quotient = 0 
        
        else: 
          quotient = n // k 
        
        remainder = n - (quotient * k) 
        n = quotient
        
        digits += remainder 
   
      return digits
