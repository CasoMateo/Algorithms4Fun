class Solution:
    def maxVowels(self, s: str, k: int) -> int:

      vowels = set(['a', 'e', 'i', 'o', 'u'])
          
      cur = 0 
      
      for j in range(k):
        if s[j] in vowels: 
          cur += 1 
    
      longest = cur 
      
      for z in range(k, len(s)):
        
        if s[z] in vowels: 
          cur += 1 
        if s[z - k] in vowels: 
          cur -= 1 

        longest = max(longest, cur) 
    
      return longest
   
