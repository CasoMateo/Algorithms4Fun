class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      
      s = list(s)
      cur = 0 
      
      while cur < len(s):
        ac = s[cur: cur + 2 * k]
        reverse = ac[: k][:: -1]
        ac[: k] = reverse
        
        s[cur: cur + 2 * k] = ac
        cur += 2 * k
          
      return ''.join(s)    
      
