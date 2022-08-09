class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mem = {}
        
        for i in range(len(s)): 
            mem[s[i]] = i 
        
        partitions = []
        prev = cur = 0 
        
        for j in range(len(s)): 
            if j > cur: 
                partitions.append(cur - prev + 1) 
                prev = cur = j
                
            
            if mem[s[j]] > cur: 
                cur = mem[s[j]] 
        
        if sum(partitions) < len(s): 
            partitions.append(cur - prev + 1)
            
        return partitions
            
            
