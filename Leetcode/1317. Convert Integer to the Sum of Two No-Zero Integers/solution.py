class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
      temp = n - 1
      
      while '0' in str(temp) or '0' in str(n - temp): 
        temp -= 1
      
      return [n - temp, temp]
        
      
        
