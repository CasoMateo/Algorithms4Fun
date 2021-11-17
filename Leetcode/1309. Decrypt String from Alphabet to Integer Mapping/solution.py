class Solution:
    def freqAlphabets(self, s: str) -> str:
      
      decoded = []
      i = 0
      
      while i < len(s):
        if i >= len(s) - 2 or s[i + 2] != '#':
          decoded.append(chr(int(s[i]) + 96))
          i += 1 
        else:
          decoded.append(chr(int(s[i] + s[i + 1]) + 96))
          i += 3
          
      return ''.join(decoded)
        
