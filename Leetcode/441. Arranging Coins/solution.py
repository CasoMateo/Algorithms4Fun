class Solution:
    def arrangeCoins(self, n: int) -> int: 
      counter = cur_sum = 0
      
      if n == 1: 
        return 1
      
      for x in range(1, n): 
        cur_sum += x 
        if cur_sum <= n: 
          counter += 1 
        else:
          break
        
      return counter
