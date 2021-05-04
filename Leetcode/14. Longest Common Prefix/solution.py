class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
      if not strs:
        return ''
      
      cur = strs[0]
      
      for i in range(1, len(strs)):
        cur = self.intersection(cur, strs[i])
      
      return cur
    
    def intersection(self, str1, str2):
      res = ''
      
      for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
          res += str1[i]
        else: 
          break
      
      return res

          
       
