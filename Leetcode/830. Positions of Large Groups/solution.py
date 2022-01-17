class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        index = 0 
        ranges = []
     
        
        for i in range(len(s) - 1):
    
            if s[i] != s[i + 1]: 
                if i - index >= 2:
                    ranges.append([index, i])
                index = i + 1
        
        if len(s) - 1 - index >= 2:
            ranges.append([index, len(s) - 1])
        
        return ranges
