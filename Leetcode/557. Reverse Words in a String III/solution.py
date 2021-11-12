class Solution:
    def reverseWords(self, s: str) -> str:
      
      words = s.split(' ')
      
      reverse = []
      
      for word in words: 
        cur = word[:: -1]
        reverse.append(cur)
      
      return ' '.join(reverse)
