class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odds = []
        evens = []
        
        for num in nums: 
          if num % 2 == 0: 
            evens.append(num)
          
          else: 
            odds.append(num)
        
        new = []
        cur = -1
        
        for i in range(len(evens)):
          new.append(evens[cur])
          new.append(odds[cur])
      
          cur -= 1
        
        return new
