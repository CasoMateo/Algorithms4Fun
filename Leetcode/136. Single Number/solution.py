class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      mem = {}
   
      for num in nums:
        if num in mem: 
          mem[num] += 1 
        else: 
          mem[num] = 1
      
      for oc in mem: 
        if mem[oc] == 1: 
          return oc
       
      
    

        
        
      
      
