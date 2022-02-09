class Solution:
    def addDigits(self, num: int) -> int:
        
        num = str(num)
        
        while len(num) > 1: 
            cur = 0 
            
            for digit in num: 
                cur += int(digit)
            
            num = str(cur)
        
        return int(num)
