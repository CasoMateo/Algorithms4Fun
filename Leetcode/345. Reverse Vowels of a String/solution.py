class Solution:
    def reverseVowels(self, s: str) -> str:
      
      vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
      found = []
    
      for letter in s: 
        if letter in vowels: 
          found.append(letter)
       
      cur = -1
      new = []
      
      for i in range(len(s)):
        if s[i] in vowels: 
          new.append(found[cur])
          cur -= 1
        
        else: 
          new.append(s[i])
      
      return ''.join(new)
      
