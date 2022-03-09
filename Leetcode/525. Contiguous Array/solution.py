class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        mem = {}
        longest = cur = 0 
        
        for i in range(len(nums)): 
            if nums[i] == 0: 
                cur -= 1 
            
            else: 
                cur += 1 
            
            if cur == 0: 
                longest = i + 1 
            
            else: 
               
                if cur in mem: 
                    longest = max(longest, i - mem[cur])
                   
                   
            if cur not in mem:
                mem[cur] = i 
       
        return longest
        
