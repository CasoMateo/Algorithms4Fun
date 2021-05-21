class Solution(object):
    def minAddToMakeValid(self, S):
        a = b = 0
        for char in S:
            if char == '(':
              b += 1 
            else: 
              b -= 1 
       
            if b == -1:
                a += 1
                b += 1
        return a + b
      
