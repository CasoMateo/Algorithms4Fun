class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        concat1 = []
        
        for string1 in word1: 
          concat1.append(string1)
          
        concat2 = []
        
        for string2 in word2: 
          concat2.append(string2) 

        return ''.join(concat1) == ''.join(concat2)
