class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r * c: 
          return mat 
        
        spread = []
        
        for row in mat: 
          spread.extend(row) 
        
        reshaped = []
        cur = c 
  
        while cur <= len(spread):
          reshaped.append(spread[cur - c: cur])
          cur += c 
        
        return reshaped
