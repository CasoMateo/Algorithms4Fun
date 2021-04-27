
class Solution:
    def sumZero(self, n: int) -> List[int]:
      ans = [] 
      limit = n//2 + 1
      
      if n % 2 == 1: 
        ans.append(0) 
        
      for i in range(1, limit): 
        ans.append(i)
        ans.append(-i)
        
      return ans
