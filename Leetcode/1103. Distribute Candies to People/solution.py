class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
      
      distribution = [0] * num_people
      cur = 0
      
      while candies > 0: 
        
        for i in range(num_people): 
          cur += 1 
          if cur > candies:
            distribution[i] += candies
            candies = 0
            break
            
          else:
            distribution[i] += cur
            candies -= cur 
          
      return distribution
        
