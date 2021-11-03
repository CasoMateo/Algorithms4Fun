class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        mem = {}
        
        for i in range(len(order)):
          mem[order[i]] = i
        
        for j in range(len(words[0])):
          cur = True
          for y in range(1, len(words)):
            if len(words[y]) - 1 < j or mem[words[y - 1][j]] > mem[words[y][j]]:
              return False 
            
            elif mem[words[y - 1][j]] == mem[words[y][j]]:
              cur = False 
       
          if cur: 
            return True
        
        return True
