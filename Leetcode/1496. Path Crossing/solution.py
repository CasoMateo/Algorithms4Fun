class Solution:
    def isPathCrossing(self, path: str) -> bool:
      
      mapping = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
      visited = set()
      visited.add('00')
      cur = ['0', '0']
      
      for coo in path: 
        
        if coo == 'N' or coo == 'S':
          new = int(cur[1]) + mapping[coo]
          cur[1] = str(new)
        
        else: 
          new = int(cur[0]) + mapping[coo]
          cur[0] = str(new)
       
        if ''.join(cur) in visited: 
          return True 
        
        visited.add(''.join(cur))
      
      return False
        
