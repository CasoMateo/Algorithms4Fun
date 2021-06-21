class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
      
      good_chars = 0
      for string in words:
        is_good = True
        temp = chars
        for char in string: 
          if char not in temp:
            is_good = False 
            break
          else: 
            temp = temp.replace(char, '', 1)

        if is_good:
          good_chars += len(string)
      
      return good_chars
        
        
