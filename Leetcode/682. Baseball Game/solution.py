class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        prev = []
        
        for i in range(len(ops)):
          if ops[i].isdigit() or ops[i].strip('-').isdigit():
            prev.append(int(ops[i]))
          
          elif ops[i] == 'C':
            prev.pop()
          
          elif ops[i] == 'D':
            prev.append(prev[-1] * 2)
          
          elif ops[i] == '+': 
            prev.append(prev[-2] + prev[-1])
      
        return sum(prev)
