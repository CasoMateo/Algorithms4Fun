    def licenseKeyFormatting(self, s: str, k: int) -> str:
      
      chars = []
      
      for i in range(len(s)):
        if s[i] != '-':
          if s[i].isalpha():
            chars.append(s[i].upper())
          else:
            chars.append(s[i]) 
      
      new = []
      cur = 0
      
      for l in range(len(chars)):
        cur += 1 
        if cur <= k:
          new.append(chars[len(chars) - l - 1])
        else:
          new.append('-')
          new.append(chars[len(chars) - l - 1])
          cur = 1

      return ''.join(new[:: -1])
