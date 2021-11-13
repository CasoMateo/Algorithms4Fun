class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
      
      total = 0 
      
      for i in range(len(mat)):
        total += mat[i][i]
      
      for j in range(len(mat)):
        total += mat[len(mat) - j - 1][j]

      if len(mat) % 2 == 1:
        total -= mat[len(mat) // 2][len(mat) // 2]
      
      return total
