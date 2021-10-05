class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m * n != len(original):
          return 
        
        doubled = []
        cur = n
        
        while cur <= len(original):

          doubled.append(original[cur - n: cur])
          cur += n
             
        return doubled
