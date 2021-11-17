class Solution:
    def maximumTime(self, time: str) -> str:
    
      mem = {0: '2', 1: '9', 3: '5', 4: '9'}
      new = list(time)
    
      for i in range(len(new)):
        if new[i] == ':':
          continue
          
        if new[i] == '?':
          if i == 0: 
            if new[i + 1] != '?' and int(new[i + 1]) >= 4:
              new[i] = '1'
              continue
            
          elif i == 1:
            if prev == '2':
              new[i] = '3'
              continue
                
          new[i] = mem[i]
        prev = new[i]
        
      return ''.join(new)
        
        
