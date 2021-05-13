class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        new = " "
        for i in s:
            if i.isalnum() == True:
                new += i
        new = new.lower()
        if new == new[::-1]:
            return True
    
        return False
