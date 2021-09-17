class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        divisors = []
        
        if len(str1) > len(str2):
          str1, str2 = str2, str1
          
        cur = ''
        for i in range(len(str1)):
          cur += str1[i]
          
          if cur * (len(str1) // len(cur)) == str1:
            divisors.append(cur)
        
        for greatest in range(len(divisors)):
          ac = divisors[len(divisors) - greatest - 1] 
          if ac * (len(str1) // len(ac)) == str1 and ac * (len(str2) // len(ac)) == str2:
            return ac 
        
        return ''
