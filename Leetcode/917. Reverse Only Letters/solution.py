class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

      priorities = []
      
      for i in range(len(s)):
        if s[len(s) - i - 1].isalpha():
          priorities.append(s[len(s) - i - 1]) 
      
      reverse = list(s)
      cur = seen = 0 
      
      while seen < len(priorities): 
        if reverse[cur].isalpha():
          reverse[cur] = priorities[seen]
          seen += 1
        
        cur += 1
      
      return ''.join(reverse)
      
      
            
