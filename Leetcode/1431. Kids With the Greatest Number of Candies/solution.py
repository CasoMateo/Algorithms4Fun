class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      res = []
      m = max(candies)
      
      for i in range(len(candies)):
        comp = m - candies[i]
        if comp <= extraCandies: 
          res.append(True)
        else: 
          res.append(False)
      
      return res
      
