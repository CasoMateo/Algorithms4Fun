class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        mem = {}
        
        for num in nums: 
          mem[num] = mem.get(num, 0) + 1 
        
        if 0 in mem: 
          nums[: mem[0]] = [0] * mem[0]
          
        if 1 in mem:
          if 0 in mem: 
            nums[mem[0] : mem[0] + mem[1]] = [1] * mem[1] 
          else: 
            nums[: mem[1]] = [1] * mem[1]
          
        if 2 in mem: 
          if 0 in mem and 1 in mem: 
            nums[mem[0] + mem[1]: mem[0] + mem[1] + mem[2]] = [2] * mem[2]
          elif 0 in mem: 
            nums[mem[0] : mem[0] + mem[2]] = [2] * mem[2] 
          elif 1 in mem: 
            nums[mem[1] : mem[1] + mem[2]] = [2] * mem[2] 
          else: 
            nums[: mem[2]] = [2] * mem[2]
            
          
