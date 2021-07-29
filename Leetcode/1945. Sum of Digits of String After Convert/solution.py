class Solution:
    def getLucky(self, s: str, k: int) -> int:
      
      alphabet = {
        'a' : '1', 
        'b' : '2', 
        'c' : '3', 
        'd' : '4', 
        'e' : '5', 
        'f' : '6', 
        'g' : '7', 
        'h' : '8', 
        'i' : '9', 
        'j' : '10', 
        'k' : '11', 
        'l' : '12', 
        'm' : '13', 
        'n' : '14', 
        'o' : '15',
        'p' : '16', 
        'q' : '17', 
        'r' : '18', 
        's' : '19', 
        't' : '20',
        'u' : '21', 
        'v' : '22', 
        'w' : '23', 
        'x' : '24', 
        'y' : '25',         
        'z' : '26'
      }
    
      new = []
        
      for char in s: 
        new.append(alphabet[char])
        
      final = int(''.join(new))
      
      for times in range(k):
        final = self.operation(final)
       
      return final
    
    
    def operation(self, n):
      S = 0

      for char in str(n):
        S += int(char)

      return S


      
        
      
        
