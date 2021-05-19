class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        prev = cur = 0
        
        for i in range(len(s)):
          if s[i] == ' ':
            cur = 0
          else:
            cur += 1
            prev = cur
          
        return prev
            
