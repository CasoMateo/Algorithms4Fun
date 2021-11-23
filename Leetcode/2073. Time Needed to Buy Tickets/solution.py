class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      
      accum = 0 
      
      for i in range(len(tickets)):
          
        if tickets[i] >= tickets[k]:
          accum += tickets[k]
          
          if i > k:
            accum -= 1
            
        else: 
          accum += tickets[i]
      
      return accum
