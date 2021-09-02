class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    
      s = sum(arr) / 3
      
      if (s != int(s)):
        return False
      
      cur = accum = 0 
      
      for i in range(len(arr) - 1):
        cur += arr[i]
        
        if accum == 2: 
          break
          
        if cur == s: 
          cur = 0
          accum += 1 
          
      return accum == 2
      
