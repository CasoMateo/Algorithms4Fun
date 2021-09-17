class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
     
        longest = cur = ''
        
        for i in range(len(str1)):
          cur += str1[i]
          
          if cur * (len(str1) // len(cur)) == str1 and cur * (len(str2) // len(cur)) == str2:
            longest = cur
        
        return longest
