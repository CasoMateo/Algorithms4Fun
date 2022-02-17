class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1: 
            return len(s)
        
        longest = cur = 0 
        i = 0 
        while True: 
            mem = {}
            
            for j in range(i, len(s)): 
                if s[j] not in mem: 
                    cur += 1 
                    mem[s[j]] = j 
                    longest = max(longest, cur)
                
                else:
                    if i < len(s) - 1:
                        i = mem[s[j]] + 1 
                        cur = 0 
                        break
            
            if j == len(s) - 1:
                break
                        
        return longest
        
