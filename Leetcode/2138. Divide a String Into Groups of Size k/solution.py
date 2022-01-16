class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        subs = []
        
        while s: 
            subs.append(s[: k])
            s = s[k: ]
        
        if len(subs[-1]) < k:
            subs[-1] += fill * (k - len(subs[-1])) 
        
        return subs
            
            
            
            
