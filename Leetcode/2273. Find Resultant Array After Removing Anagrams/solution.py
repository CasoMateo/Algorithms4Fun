class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
      
      i = 0
      
      while True: 
        
        if i == len(words) - 1:
          if len(words) == 1 or Counter(words[i]) != Counter(words[i - 1]):
            break 
        
        else: 
          i += 1 

        if Counter(words[i]) == Counter(words[i - 1]): 
          words = words[: i] + words[i + 1: ] 
          i -= 1 
        
      return words
