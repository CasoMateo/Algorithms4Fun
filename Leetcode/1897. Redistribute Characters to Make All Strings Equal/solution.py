class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        all = ''.join(words)
        mem = {}
        
        for word in all:
            if word not in mem :
                mem[word] = all.count(word)
                
        for frequency in mem:
            if mem[frequency] % len(words) != 0 : 
              return False 
        return True 
      
    
      
      
   
            
            
