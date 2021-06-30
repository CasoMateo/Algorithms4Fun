class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
      mem = {} 
      
      for i in range(len(strs)):
        string = ''
        
        for char in sorted(strs[i]):
          string += char
          
        if string not in mem: 
          mem[string] = [strs[i]]
        else: 
          mem[string].append(strs[i])
          
      anagrams = []
      
      for group in mem: 
        anagrams.append(mem[group]) 
      
      return anagrams
        
