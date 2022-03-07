class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
      
 
        if len(nums) < 3: 
            return 0 
        
        arithmetic = 0 
        cur = set([nums[0], nums[1]])
        ac = 2
        dif = abs(nums[1] - nums[0])
        
        for i in range(2, len(nums)): 
            if abs(nums[i] - nums[i - 1]) == dif: 
                if nums[i] in cur and nums[i - 1] != nums[i]:
                    dif = float('inf')
                    continue 
                    
                cur.add(nums[i])
                ac += 1 
                
                arithmetic += ac - 3 + 1
             
            
            else: 
                cur = set([nums[i], nums[i - 1]])
                dif = abs(nums[i] - nums[i - 1])
                ac = 2
        
        return arithmetic
                
