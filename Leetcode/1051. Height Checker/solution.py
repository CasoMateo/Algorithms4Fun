class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        
        dif = 0 
        for i in range(len(heights)):
          if expected[i] != heights[i]:
            dif += 1 
        
        return dif
            
