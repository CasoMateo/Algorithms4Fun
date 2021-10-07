class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      
      words = []
      cur = ''
      
      for i in range(len(paragraph)):
        if not paragraph[i].isalpha():
          if cur:
            words.append(cur)
            
          cur = ''
          
        else: 
          cur += paragraph[i]
      
      if cur: 
        words.append(cur)
        
      mem = {}
      
      for word in words: 
        mem[word.lower()] = mem.get(word.lower(), 0) + 1 
      
      mem = dict(sorted(mem.items(), key = operator.itemgetter(1), reverse = True))
      
      for common in mem: 
        if common not in banned: 
          return common 
        
