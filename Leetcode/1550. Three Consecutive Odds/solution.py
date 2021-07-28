class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
      
      cur = 0 
      
      for i in range(len(arr)):
        if arr[i] % 2 == 1: 
          cur += 1 
          if cur == 3: 
            return True
        else: 
          cur = 0 
      
      return False
