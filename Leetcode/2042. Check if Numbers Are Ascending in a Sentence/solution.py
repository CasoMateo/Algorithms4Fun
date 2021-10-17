class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        tokens = s.split(' ')
        
        numbers = []
        
        for token in tokens: 
          if token.isdigit():
            numbers.append(int(token))
        
        for i in range(1, len(numbers)):
          if numbers[i - 1] >= numbers[i]:
            return False 
        
        return True
