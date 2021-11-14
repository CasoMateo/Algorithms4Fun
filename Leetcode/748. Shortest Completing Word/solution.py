class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
      
      shortest = ' ' * 1000
      
      mem = {}
      
      for i in range(len(licensePlate)):
        if licensePlate[i].isalpha():
          mem[licensePlate[i].lower()] = mem.get(licensePlate[i].lower(), 0) + 1
        
      for word in words:
        cur = {}
        
        for char in word: 
          cur[char.lower()] = cur.get(char.lower(), 0) + 1
        
        pos = True  
        
        for freq in mem: 
          if freq not in cur or mem[freq] > cur[freq]:
            pos = False 
            break
        
        if pos:
          if len(word) < len(shortest):
            shortest = word
        
      return shortest
        
