class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
      
        mem = {}
        
        for num in nums: 
          mem[num] = mem.get(num, 0) + 1 
          
        unique = 0  
    
        for freq in mem: 
          if mem[freq] == 1: 
            unique += freq 
        
        return unique 
        
