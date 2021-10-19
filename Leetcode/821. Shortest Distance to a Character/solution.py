class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
      
      answer = []
      indices = []
      
      for e in range(len(s)):
        if s[e] == c: 
          indices.append(e)
      
      for i in range(len(s)):
        cur = float('inf')
        for index in indices:
          if s[index] == c:
            cur = min(cur, abs(i - index))
        
        answer.append(cur)
    
      return answer
        
