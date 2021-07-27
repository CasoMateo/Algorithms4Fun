class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
      
      drink = remaining = 0
      
      while numBottles > 0: 
        drink += numBottles 
        reusable = (numBottles + remaining) // numExchange
        remaining += numBottles - (reusable * numExchange)
        numBottles = reusable
        
      return drink 
