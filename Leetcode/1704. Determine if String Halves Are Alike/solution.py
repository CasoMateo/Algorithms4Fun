class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      
      first = s[: len(s) // 2]
      second = s[len(s) // 2: ]
      
      return self.vowels(first) == self.vowels(second)
    
    def vowels(self, string):
      
      cur = 0
      vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
      
      for i in range(len(string)):
        if string[i] in vowels: 
          cur += 1
      
      return cur
