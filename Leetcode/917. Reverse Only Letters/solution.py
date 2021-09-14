class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

      priorities = []
      
      for i in range(len(s)):
        if s[i].isalpha():
          priorities.append(s[i]) 
      
      reverse = []
      
      for cur in range(len(s)):
        if s[cur].isalpha():
          reverse.append(priorities[-1])
          priorities.pop()
        else: 
          reverse.append(s[cur])
      
      return ''.join(reverse)
