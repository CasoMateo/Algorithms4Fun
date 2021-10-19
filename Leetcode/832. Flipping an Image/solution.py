class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(A)):
          cur = []
          
          for j in range(len(A[i])):
            cur.append(A[i][len(A[i]) - j - 1])
          
          A[i] = cur 
        
        for x in range(len(A)):
          for y in range(len(A[x])):
            if A[x][y] == 0:
              A[x][y] = 1 
            
            else: 
              A[x][y] = 0 
        
        return A
