class Solution:
    def secondHighest(self, s: str) -> int:
      
      digits = set()
      
      for char in s: 
        if char.isdigit():
          digits.add(char)
      
      if len(digits) < 2: 
        return -1 
      
      digits.remove(max(digits))
      return max(digits)
        
