class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
      
      cols = []
      
      for i in range(len(matrix[0])):
        cur = []
        for j in range(len(matrix)):
          cur.append(matrix[j][i])
        
        cols.append(cur)
      
      lucky = []
      
      for row in range(len(matrix)):
        ac = matrix[row]
        
        if min(ac) == max(cols[ac.index(min(ac))]):
          lucky.append(min(ac))
      
      return lucky
