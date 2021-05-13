class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        x = " "
        for i in s:
            if i.isalnum() == True:
                x += i
        x = x.lower()
        if x == x[::-1]:
            return True
    
        return False
