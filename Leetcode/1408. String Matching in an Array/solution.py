class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        substrings = []
        
        for word in words:
          for other in words: 
            if other == word: 
              continue 
            
            if word in other: 
              substrings.append(word)
              break
        
        return substrings
          
