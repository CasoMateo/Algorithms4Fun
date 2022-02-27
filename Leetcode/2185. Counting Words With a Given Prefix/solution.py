class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0 
        
        for word in words: 
            cur = word[: len(pref)]
            
            if cur == pref: 
                count += 1 
        
        return count
