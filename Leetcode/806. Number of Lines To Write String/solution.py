class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
      
      cur = lines = 0 
      for j in range(len(s)):
        cur += widths[ord(s[j]) - ord('a')]
              
        if cur > 100: 
          lines += 1 
          cur = widths[ord(s[j]) - ord('a')]
      
      lines += 1
  
      return [lines, cur]
