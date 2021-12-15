class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
      
      temp = matrix.copy()
      
      for i in range(len(temp)):
        cur = []
        for j in range(len(temp)):
          cur.append(temp[j][i])
        
        cur = cur[:: -1]
        matrix[i] = cur 
      
      return matrix
