class Solution:
    def countEven(self, num: int) -> int:
        
        if num == 1: 
            return 0 
        
        even = 0 
        
        for digits in range(1, num + 1):
            cur = 0
            
            for digit in str(digits):
                cur += int(digit)
            
            if cur % 2 == 0: 
                even += 1 
        
        return even 
                
    
