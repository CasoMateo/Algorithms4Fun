class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
      
      return self.reverse(self.reverse(num)) == str(num)
    
    def reverse(self, num):
      cur = ''
      
      for digit in str(num):
        cur += digit
      
      cur = cur[:: -1]
   
      while len(cur) > 1 and cur[0] == '0':
        cur = cur[1: ]
        
      return cur 
        
