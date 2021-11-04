class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
      
      mem = {}
      
      for card in deck: 
        mem[card] = mem.get(card, 0) +1 

      for i in range(2, mem[deck[0]] + 1):
        cur = True
        
        for freq in mem: 
          if mem[freq] % i != 0: 
            cur = False 
            break 
        
        if cur: 
          return True
          
      return False
