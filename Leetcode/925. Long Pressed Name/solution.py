class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if name[0] != typed[0]: 
            return False 
        
        cur = prev = 0
        last = False
        
        for i in range(len(typed)): 
            
            if last: 
                if typed[i] != name[-1]:
                    return False
                continue
                
            if typed[i] == name[cur]: 
                cur += 1 
                prev = i
            
            else: 
                if typed[i] != typed[prev]: 
                    return False 
                
            if cur == len(name): 
                last = True
                
        return cur == len(name)
