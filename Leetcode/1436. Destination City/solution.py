class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        mem = {}
        
        for i in range(len(paths)):
            mem[paths[i][0]] = paths[i][1]
        
        for j in range(len(paths)):
            if paths[j][1] not in mem: 
                return paths[j][1]
            
