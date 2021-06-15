class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = []
        
        for i in range(len(words[0])):
          cur = words[0][i]
          common = 0 
          for j in range(1, len(words)):
            if cur in words[j]:
              common += 1 
              words[j] = words[j][:words[j].find(cur)] + words[j][words[j].find(cur) + 1:]
              
          if common == len(words) - 1:
            res.append(cur)
      
        return res
