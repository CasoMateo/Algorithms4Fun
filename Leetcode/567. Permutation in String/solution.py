class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        mem = Counter(s1)
        ref = Counter(s2[: len(s1)])
        
        for i in range(len(s1), len(s2)) :
            if ref == mem: 
                return True 
            
            ref[s2[i - len(s1)]] -= 1 
            if ref[s2[i - len(s1)]] == 0: 
                ref.pop(s2[i - len(s1)])
            
            ref[s2[i]] = ref.get(s2[i], 0) + 1
        
        if mem == ref: 
            return True
        
        return False
