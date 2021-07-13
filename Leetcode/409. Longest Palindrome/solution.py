class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = {}
        
        for i in range(len(s)):
          if s[i] in freq: 
            freq[s[i]] += 1 
          else: 
            freq[s[i]] = 1 
          
        longest = 0 
        
        for oc in freq:
          if freq[oc] % 2 == 0 and freq[oc] != 1: 
            longest += freq[oc]
            freq[oc] = 0
          elif freq[oc] % 2 == 1 and freq[oc] != 1: 
            longest += freq[oc] - 1
            freq[oc] = 1 
          
        for center in freq:
          if freq[center] == 1: 
            return longest + 1 
        
        return longest
        
