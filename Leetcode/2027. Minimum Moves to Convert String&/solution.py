class Solution(object):
    def minimumMoves(self, s):
    
      operations, cur = 0, 0
      
      while cur < len(s):
        if s[cur] == 'X':
          cur += 3
          operations +=1
        else:
          cur += 1
      
      return operations
