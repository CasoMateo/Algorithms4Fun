class Solution:
    def minOperations(self, s: str) -> int:
        
        first = '01' * (len(s) // 2)
        second = '10' * (len(s) // 2)
        
        if len(s) % 2 == 1: 
          first += '0'
          second += '1'
          
        operations1 = operations2 = 0 
        
        for i in range(len(s)):
          if s[i] != first[i]:
            operations1 += 1 
        
        for j in range(len(s)):
          if s[j] != second[j]:
            operations2 += 1 
        
        return min(operations1, operations2)
        
