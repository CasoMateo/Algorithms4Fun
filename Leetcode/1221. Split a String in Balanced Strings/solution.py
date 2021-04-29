class Solution:
    def balancedStringSplit(self, s: str) -> int:
      sum_ = counter = 0 
      
      for i in range(len(s)):
        if s[i] == 'R':
          sum_ -= 1 
        elif s[i] == 'L':
          sum_ += 1 
        if sum_ == 0: 
          counter += 1 
      return counter
  
