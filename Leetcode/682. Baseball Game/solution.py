class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        
        for operation in ops:
       
          if operation == 'C':
            stack.pop()
          
          elif operation == 'D':
            stack.append(stack[-1] * 2)
          
          elif operation == '+': 
            stack.append(stack[-2] + stack[-1])
      
          else: 
            stack.append(int(operation))
            
        return sum(stack)
