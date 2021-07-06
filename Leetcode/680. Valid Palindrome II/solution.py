
class Solution:
    def validPalindrome(self, s: str) -> bool:
      
      if s == s[::-1]:
        return True
    
      for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
         
          if self.possiblePalindrome(s, i) or self.possiblePalindrome(s, len(s) - i - 1):         
            return True
          
          break
      
      return False
    
    def possiblePalindrome(self, s, i):
      temp = s[:i] + s[i + 1:]
  
      return temp == temp[::-1] 
         
