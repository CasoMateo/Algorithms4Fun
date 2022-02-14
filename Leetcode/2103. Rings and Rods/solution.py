class Solution:
    def countPoints(self, rings: str) -> int:
        
        mem = {}
        count = set()
        
        for i in range(0, len(rings) - 1, 2):
            if rings[i + 1] in mem: 
                mem[rings[i + 1]].add(rings[i])
                if len(mem[rings[i + 1]]) == 3: 
                    count.add(rings[i + 1])
            
            else: 
                mem[rings[i + 1]] = set(rings[i])
        
        return len(count)
