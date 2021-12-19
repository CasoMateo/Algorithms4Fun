class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
      
      palindrome = ''
      
      for word in words:
        if word == word[:: -1]:
          palindrome = word 
          break 
      
      return palindrome
