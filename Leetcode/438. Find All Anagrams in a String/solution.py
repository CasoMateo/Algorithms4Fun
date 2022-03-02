class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = ''.join(sorted(p))
        len_p = len(p)
        res = []
        mem = Counter(p)
        
        for i in range(len(s) - len_p + 1):
            cur_str = s[i:len_p + i]
            valid = True 
            
            for val in 'abcdefghijklmnopqrstuvwxyz':
                if mem[val] != cur_str.count(val):
                    valid = False 
                    break 
            
            if valid: 
                res.append(i)
  
        return res
            
            
            
