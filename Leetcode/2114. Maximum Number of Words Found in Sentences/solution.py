class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
      
      largest = 0 
      
      for sentence in sentences: 
        cur = sentence.split(' ')
        largest = max(largest, len(cur))
      
      return largest
