class Solution:
    def interpret(self, command: str) -> str:
        
        mem = {'G': 'G', '()': 'o', '(al)': 'al'}
        interpretation = []
        cur = ''
        
        for i in range(len(command)):
          if command[i] in mem or cur in mem:
            if cur:
              interpretation.append(mem[cur])
              cur = command[i]
            
            else:
              interpretation.append(mem[command[i]])
          
          else:
            cur += command[i]

        if cur in mem: 
          interpretation.append(mem[cur])
        
        return ''.join(interpretation)
