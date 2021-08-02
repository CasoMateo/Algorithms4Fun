class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      
      pascal = [[1]] 
      
      if numRows == 1:
        return pascal 
      
      for i in range(1, numRows):
        prev = pascal[i - 1] 
        cur = [prev[0], prev[-1]]
        
        for j in range(1, len(prev)):
          cur.insert(j, prev[j - 1] + prev[j])
      
        pascal.append(cur)
        
      return pascal
        
