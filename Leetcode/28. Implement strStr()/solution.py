class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0 
        
        for i in range(len(haystack) - len(needle) + 1):
            cur = haystack[i : i + len(needle)]
            if cur == needle: 
                return i 
        
        return -1
