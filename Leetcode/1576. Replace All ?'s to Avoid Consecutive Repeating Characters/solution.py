class Solution:
    def modifyString(self, s: str) -> str:
      
      mem = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'y', 'z'])
      new = []
      
      prev = ''
                 
      for i in range(len(s) - 1):
        if s[i] == '?':
          for letter in mem: 
            if letter != prev and letter != s[i + 1]:
              cur = letter
              continue
        else:
          cur = s[i]
          
        prev = cur
        new.append(cur)
    
      if s[len(s) - 1] == '?':
        for letter in mem: 
          if s[len(s) - 2] != letter:
            new.append(letter) 
            break
      else: 
        new.append(s[len(s) - 1])
          
      
      return ''.join(new)
          
                 
