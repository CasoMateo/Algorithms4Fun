class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
     
      res = []
      
      for i in range(left, right + 1):
        if self.selfDividing(i):
          res.append(i)
      
      return res
    
    def selfDividing(self, n):
      
      if '0' in str(n):
        return False
      
      for num in str(n):
        if n % int(num) != 0: 
          return False 
      
      return True
        
