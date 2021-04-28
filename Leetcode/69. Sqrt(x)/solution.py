class Solution:
    def mySqrt(self, x: int) -> int:
        
        if(x < 4): return 1 if (x != 0) else 0
            
        low = 2
        high = x // 2 
        while(low <= high):
            mid = low + (high - low) // 2
            if( mid**2 < x):
                low = mid + 1
            
            elif( mid**2 > x):
                high = mid - 1
            else:
                return mid
        return high
        
        
