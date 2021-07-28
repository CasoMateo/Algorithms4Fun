class Solution:
    def minOperations(self, n: int) -> int:
      
      lo = 0
      hi = n - 1
      operations = 0
      
      while lo <= hi: 
        operations += ((2 * hi + 1) - ((2 * lo) + 1)) // 2 
        lo += 1 
        hi -= 1
      
      return operations
        
        
          
        
