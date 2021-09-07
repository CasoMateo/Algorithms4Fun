
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
      
      total = 0 
      
      for num in nums: 
        cur = set()
        for div in range(1, floor(sqrt(num)) + 1):
          
          if num % div == 0: 
            cur.add(div)
            cur.add(num // div)
            
            if len(cur) > 4: 
              break
       
        if len(cur) == 4: 

          total += sum(cur) 
        
      return total
