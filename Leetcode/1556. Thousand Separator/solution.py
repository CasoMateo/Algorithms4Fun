class Solution:
    def thousandSeparator(self, n: int) -> str:
      
      separated = []
      
      cur = 0 
      
      for i in range(len(str(n))):
        if cur < 3: 
          cur += 1 
        
        else: 
          cur = 1 
          separated.append('.')
        
        separated.append(str(n)[len(str(n)) - i - 1])
      
      return ''.join(reversed(separated))
